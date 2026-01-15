"""Code Arena Module - AI-powered coding challenges"""
import os
import json
import re
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import CodeChallenge, ChallengeResult

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "meta-llama/llama-3.2-3b-instruct:free"

DIFFICULTY_XP = {
    "Easy": 20,
    "Medium": 40,
    "Hard": 70
}

def generate_challenge(difficulty: str = "Easy", topic: str = "general") -> CodeChallenge:
    """Generate a coding challenge using OpenRouter"""
    
    prompt = f"""You are a coding challenge creator. Create a {difficulty} Python coding challenge about {topic}.

Return a JSON object in this EXACT format (no markdown, just pure JSON):
{{
    "title": "Challenge Title",
    "description": "Clear problem description. Explain what the function should do.",
    "starter_code": "def solution(input):\\n    # Your code here\\n    pass",
    "test_cases": [
        "assert solution(1) == 1",
        "assert solution(2) == 4"
    ],
    "hints": [
        "First hint",
        "Second hint"
    ]
}}

Difficulty guidelines:
- Easy: Basic loops, conditionals, simple math
- Medium: Data structures, string manipulation, basic algorithms
- Hard: Recursion, dynamic programming, complex algorithms

Make sure test_cases are valid Python assert statements. Return ONLY valid JSON, no other text."""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        text = response.choices[0].message.content.strip()
        if text.startswith("```"):
            text = re.sub(r'^```json?\n?', '', text)
            text = re.sub(r'\n?```$', '', text)
        
        data = json.loads(text)
        
        return CodeChallenge(
            id=hash(data["title"]) % 10000,
            title=data["title"],
            description=data["description"],
            difficulty=difficulty,
            starter_code=data["starter_code"],
            test_cases=data["test_cases"],
            hints=data["hints"],
            xp_reward=DIFFICULTY_XP.get(difficulty, 20)
        )
    except Exception as e:
        print(f"[CHALLENGE ERROR] {type(e).__name__}: {e}")
        return CodeChallenge(
            id=1001,
            title="Sum Two Numbers",
            description=f"Error: {str(e)[:80]}. Write a function that takes two numbers and returns their sum.",
            difficulty="Easy",
            starter_code="def solution(a, b):\n    # Your code here\n    pass",
            test_cases=[
                "assert solution(1, 2) == 3",
                "assert solution(0, 0) == 0",
                "assert solution(-1, 1) == 0"
            ],
            hints=["Use the + operator", "Return the result"],
            xp_reward=20
        )

def evaluate_solution(challenge: CodeChallenge, user_code: str) -> ChallengeResult:
    """Evaluate user's code solution using AI"""
    
    prompt = f"""You are a code evaluator. Evaluate this solution for the given challenge.

CHALLENGE: {challenge.title}
DESCRIPTION: {challenge.description}
TEST CASES: {challenge.test_cases}

USER'S CODE:
```python
{user_code}
```

Evaluate if the code would pass the test cases. Consider:
1. Correctness - Does it solve the problem?
2. Edge cases - Does it handle them?
3. Code quality - Is it clean and efficient?

Return JSON in this EXACT format (no markdown, just pure JSON):
{{
    "passed": true,
    "feedback": "Detailed feedback for the user",
    "tests_passed": 3,
    "total_tests": 3,
    "is_optimal": true
}}

Return ONLY valid JSON, no other text."""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        text = response.choices[0].message.content.strip()
        if text.startswith("```"):
            text = re.sub(r'^```json?\n?', '', text)
            text = re.sub(r'\n?```$', '', text)
        
        data = json.loads(text)
        
        base_xp = challenge.xp_reward if data["passed"] else 0
        bonus_xp = 20 if data.get("is_optimal") and data["passed"] else 0
        
        return ChallengeResult(
            passed=data["passed"],
            feedback=data["feedback"],
            xp_earned=base_xp,
            bonus_xp=bonus_xp
        )
    except Exception as e:
        print(f"[EVAL ERROR] {type(e).__name__}: {e}")
        return ChallengeResult(
            passed=False,
            feedback=f"Error evaluating solution: {str(e)[:100]}",
            xp_earned=0,
            bonus_xp=0
        )

def get_challenge_topics() -> list:
    """Get available challenge topics"""
    return [
        {"id": "general", "name": "General Programming", "icon": "🎯"},
        {"id": "strings", "name": "String Manipulation", "icon": "📝"},
        {"id": "arrays", "name": "Arrays & Lists", "icon": "📊"},
        {"id": "math", "name": "Math & Numbers", "icon": "🔢"},
        {"id": "algorithms", "name": "Algorithms", "icon": "⚡"},
        {"id": "data_structures", "name": "Data Structures", "icon": "🏗️"},
    ]
