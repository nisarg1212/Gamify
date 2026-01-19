"""Master Mode - Advanced practice questions"""
import os
import json
import re
import time
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import MasterPractice, MasterQuestion

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "google/gemini-2.0-flash-exp:free"

def generate_master_practice(topic: str, key_facts: List[str]) -> MasterPractice:
    """Generate advanced practice questions"""
    
    # Add small delay to avoid rate limiting
    time.sleep(1)
    
    facts_text = "\n".join([f"- {fact}" for fact in key_facts[:3]])
    
    prompt = f"""Generate 3 advanced multiple choice questions about {topic}.

Key facts: {facts_text}

Return JSON only:
{{"questions":[{{"question":"Q1?","options":["A","B","C","D"],"correct_answer":"A","explanation":"Why A"}}]}}"""

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            
            if not response or not response.choices:
                raise ValueError("Empty response")
            
            text = response.choices[0].message.content
            if not text:
                raise ValueError("Empty content")
            
            text = text.strip()
            
            # Remove markdown code blocks
            if "```" in text:
                text = re.sub(r'```json?\s*', '', text)
                text = re.sub(r'```', '', text)
            
            # Extract JSON
            json_match = re.search(r'\{[\s\S]*\}', text)
            if json_match:
                text = json_match.group()
            
            data = json.loads(text)
            
            questions = []
            for q in data.get("questions", [])[:3]:
                questions.append(MasterQuestion(
                    question=q.get("question", "Question"),
                    question_type="multiple_choice",
                    options=q.get("options", ["A", "B", "C", "D"]),
                    correct_answer=q.get("correct_answer", "A"),
                    explanation=q.get("explanation", "Correct!"),
                    xp_reward=20
                ))
            
            if questions:
                return MasterPractice(
                    topic=topic,
                    questions=questions,
                    total_xp=len(questions) * 20 + 50
                )
            
        except Exception as e:
            print(f"[MASTER ATTEMPT {attempt+1}] {type(e).__name__}: {e}")
            if attempt < 1:
                time.sleep(2)
                continue
    
    # Fallback
    print(f"[MASTER] Using fallback for {topic}")
    return MasterPractice(
        topic=topic,
        questions=[
            MasterQuestion(
                question=f"How can {topic} knowledge be applied practically?",
                question_type="multiple_choice",
                options=["Solve real problems", "Cannot be applied", "Only theory", "Random use"],
                correct_answer="Solve real problems",
                explanation="Knowledge is power when applied!",
                xp_reward=20
            ),
            MasterQuestion(
                question=f"What's key to mastering {topic}?",
                question_type="multiple_choice",
                options=["Deep understanding", "Memorization", "Guessing", "Skipping"],
                correct_answer="Deep understanding",
                explanation="Understanding beats memorization!",
                xp_reward=20
            )
        ],
        total_xp=90
    )

def score_master(master: MasterPractice, answers: List[str]) -> dict:
    """Score master practice answers"""
    correct = 0
    results = []
    
    for question, answer in zip(master.questions, answers):
        is_correct = answer.strip().lower() == question.correct_answer.strip().lower()
        if is_correct:
            correct += 1
        results.append({
            "question": question.question,
            "your_answer": answer,
            "correct_answer": question.correct_answer,
            "is_correct": is_correct,
            "explanation": question.explanation
        })
    
    total = len(master.questions)
    percentage = (correct / total) * 100 if total > 0 else 0
    
    return {
        "correct": correct,
        "total": total,
        "percentage": round(percentage, 1),
        "xp_earned": correct * 20 + (50 if percentage == 100 else 0),
        "bonus_xp": 50 if percentage == 100 else 0,
        "mastered": percentage >= 80,
        "results": results
    }
