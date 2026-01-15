"""Document Quest Module - Turn documents into interactive quizzes"""
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

MODEL = "meta-llama/llama-3.2-3b-instruct:free"

def generate_quiz(content: str, num_questions: int = 5) -> Quiz:
    """Generate a quiz from document content using OpenRouter"""
    
    prompt = f"""You are a quiz generator. Based on the following content, create {num_questions} multiple choice questions.

CONTENT:
{content[:4000]}

Return a JSON object in this EXACT format (no markdown, just pure JSON):
{{
    "title": "Quiz title based on content",
    "questions": [
        {{
            "question": "The question text",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_index": 0,
            "explanation": "Brief explanation of why this is correct"
        }}
    ]
}}

Make the questions educational and progressively more difficult. Ensure correct_index is 0-3. Return ONLY valid JSON, no other text."""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract JSON from response
        text = response.choices[0].message.content.strip()
        # Remove markdown code blocks if present
        if text.startswith("```"):
            text = re.sub(r'^```json?\n?', '', text)
            text = re.sub(r'\n?```$', '', text)
        
        data = json.loads(text)
        
        questions = [
            QuizQuestion(
                question=q["question"],
                options=q["options"],
                correct_index=q["correct_index"],
                explanation=q.get("explanation", "")
            )
            for q in data["questions"]
        ]
        
        return Quiz(
            title=data["title"],
            questions=questions,
            total_xp=len(questions) * 10 + 20
        )
    except Exception as e:
        print(f"[QUIZ ERROR] {type(e).__name__}: {e}")
        return Quiz(
            title="Quick Knowledge Check",
            questions=[
                QuizQuestion(
                    question=f"Error: {str(e)[:100]}. What was the main topic?",
                    options=["Topic A", "Topic B", "Topic C", "I need to review more"],
                    correct_index=3,
                    explanation="Keep learning!"
                )
            ],
            total_xp=10
        )

def score_quiz(quiz: Quiz, answers: List[int]) -> dict:
    """Score quiz answers and calculate XP"""
    correct = 0
    results = []
    
    for i, (question, answer) in enumerate(zip(quiz.questions, answers)):
        is_correct = answer == question.correct_index
        if is_correct:
            correct += 1
        results.append({
            "question": question.question,
            "your_answer": question.options[answer] if 0 <= answer < len(question.options) else "No answer",
            "correct_answer": question.options[question.correct_index],
            "is_correct": is_correct,
            "explanation": question.explanation
        })
    
    total = len(quiz.questions)
    percentage = (correct / total) * 100 if total > 0 else 0
    
    base_xp = correct * 10
    bonus_xp = 30 if percentage == 100 else (15 if percentage >= 80 else 0)
    total_xp = base_xp + bonus_xp
    
    return {
        "correct": correct,
        "total": total,
        "percentage": round(percentage, 1),
        "xp_earned": total_xp,
        "bonus_xp": bonus_xp,
        "perfect": percentage == 100,
        "results": results
    }
