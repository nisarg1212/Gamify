"""Quiz Mode - Generate comprehension questions from story"""
import os
import json
import re
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import Quiz, QuizQuestion

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "google/gemini-2.0-flash-exp:free"

def generate_quiz(topic: str, key_facts: List[str], num_questions: int = 5) -> Quiz:
    """Generate a quick test quiz based on the story"""
    
    facts_text = "\n".join([f"- {fact}" for fact in key_facts[:5]])
    
    prompt = f"""Create {num_questions} multiple choice questions about: {topic}

Based on these facts:
{facts_text}

IMPORTANT: Return ONLY valid JSON in this exact format, nothing else:
{{"questions": [{{"question": "Question text?", "options": ["A", "B", "C", "D"], "correct_index": 0, "explanation": "Why correct"}}]}}"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        if not response or not response.choices:
            raise ValueError("Empty response")
        
        text = response.choices[0].message.content
        if not text:
            raise ValueError("Empty content")
        
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r'^```json?\s*\n?', '', text)
            text = re.sub(r'\n?```\s*$', '', text)
        
        # Try to find JSON
        json_match = re.search(r'\{[\s\S]*\}', text)
        if json_match:
            text = json_match.group()
        
        data = json.loads(text)
        
        questions = []
        for q in data.get("questions", [])[:num_questions]:
            questions.append(QuizQuestion(
                question=q.get("question", "Question"),
                options=q.get("options", ["A", "B", "C", "D"]),
                correct_index=q.get("correct_index", 0),
                explanation=q.get("explanation", "")
            ))
        
        if not questions:
            raise ValueError("No questions generated")
        
        return Quiz(
            topic=topic,
            questions=questions,
            difficulty="basic",
            total_xp=len(questions) * 10 + 20
        )
    except Exception as e:
        print(f"[QUIZ ERROR] {type(e).__name__}: {e}")
        # Return fallback quiz
        return Quiz(
            topic=topic,
            questions=[
                QuizQuestion(
                    question=f"What is a key aspect of {topic}?",
                    options=["Understanding concepts", "Just memorizing", "Ignoring details", "Random guessing"],
                    correct_index=0,
                    explanation="Understanding concepts is key to learning!"
                ),
                QuizQuestion(
                    question=f"Why is learning about {topic} valuable?",
                    options=["It has practical applications", "It's not valuable", "Only for experts", "No reason"],
                    correct_index=0,
                    explanation="Knowledge has practical applications!"
                ),
                QuizQuestion(
                    question=f"What helps in mastering {topic}?",
                    options=["Practice and curiosity", "Avoiding study", "Giving up", "Not asking questions"],
                    correct_index=0,
                    explanation="Practice and curiosity are essential!"
                )
            ],
            difficulty="basic",
            total_xp=50
        )

def score_quiz(quiz: Quiz, answers: List[int]) -> dict:
    """Score quiz answers and calculate XP"""
    correct = 0
    results = []
    
    for i, (question, answer) in enumerate(zip(quiz.questions, answers)):
        # Handle invalid answer indices
        if answer < 0 or answer >= len(question.options):
            answer = 0
        
        is_correct = answer == question.correct_index
        if is_correct:
            correct += 1
        results.append({
            "question": question.question,
            "your_answer": question.options[answer],
            "correct_answer": question.options[question.correct_index],
            "is_correct": is_correct,
            "explanation": question.explanation
        })
    
    total = len(quiz.questions)
    percentage = (correct / total) * 100 if total > 0 else 0
    
    base_xp = correct * 10
    bonus_xp = 20 if percentage >= 80 else 0
    total_xp = base_xp + bonus_xp
    
    return {
        "correct": correct,
        "total": total,
        "percentage": round(percentage, 1),
        "xp_earned": total_xp,
        "bonus_xp": bonus_xp,
        "passed": percentage >= 60,
        "results": results
    }
