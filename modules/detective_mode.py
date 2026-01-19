"""Detective Mode - Mystery solving with learned knowledge"""
import os
import json
import re
import time
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import DetectiveCase, Clue

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "google/gemini-2.0-flash-exp:free"

def generate_detective_case(topic: str, key_facts: List[str]) -> DetectiveCase:
    """Generate a mystery case that requires applying learned knowledge"""
    
    # Add delay to avoid rate limiting
    time.sleep(1)
    
    facts_text = ", ".join(key_facts[:3])
    
    prompt = f"""Create a short detective mystery about {topic} using these facts: {facts_text}

Return JSON only:
{{"case_title":"Title","scenario":"2-3 sentence mystery","clues":[{{"id":1,"description":"Clue"}}],"question":"What's the answer?","options":["A","B","C","D"],"correct_answer":"A","explanation":"Why"}}"""

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800
            )
            
            if not response or not response.choices:
                raise ValueError("Empty response")
            
            text = response.choices[0].message.content
            if not text:
                raise ValueError("Empty content")
            
            text = text.strip()
            
            # Remove markdown
            if "```" in text:
                text = re.sub(r'```json?\s*', '', text)
                text = re.sub(r'```', '', text)
            
            json_match = re.search(r'\{[\s\S]*\}', text)
            if json_match:
                text = json_match.group()
            
            data = json.loads(text)
            
            clues = [Clue(id=i+1, description=c.get("description", "Clue"), is_key_clue=True) 
                     for i, c in enumerate(data.get("clues", [])[:4])]
            
            if not clues:
                clues = [Clue(id=1, description="Use your knowledge", is_key_clue=True)]
            
            options = data.get("options", [])
            question = data.get("question", "What is the solution?")
            if options:
                question += "\n\n" + "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(options[:4])])
            
            return DetectiveCase(
                topic=topic,
                case_title=data.get("case_title", f"The {topic} Mystery"),
                scenario=data.get("scenario", "A mystery awaits..."),
                clues=clues,
                question=question,
                correct_answer=data.get("correct_answer", "A"),
                explanation=data.get("explanation", "Great detective work!"),
                xp_reward=100
            )
            
        except Exception as e:
            print(f"[DETECTIVE ATTEMPT {attempt+1}] {type(e).__name__}: {e}")
            if attempt < 1:
                time.sleep(2)
                continue
    
    # Fallback
    print(f"[DETECTIVE] Using fallback for {topic}")
    return DetectiveCase(
        topic=topic,
        case_title=f"The {topic} Case",
        scenario=f"Professor Knowledge left a puzzle about {topic}. Use your knowledge to solve it!",
        clues=[
            Clue(id=1, description=f"Think about core concepts of {topic}", is_key_clue=True),
            Clue(id=2, description="Connect what you've learned", is_key_clue=True)
        ],
        question=f"What's the key insight about {topic}?\n\nA. Understanding is key\nB. Random guessing\nC. Skip learning\nD. Give up",
        correct_answer="Understanding is key",
        explanation=f"Your {topic} knowledge shows understanding is the key to mastery!",
        xp_reward=100
    )

def solve_case(case: DetectiveCase, answer: str) -> dict:
    """Check if the case was solved correctly"""
    answer_lower = answer.strip().lower()
    correct_lower = case.correct_answer.strip().lower()
    
    # Logic for single letter answers (e.g. "A", "B")
    if len(answer_lower) == 1:
        # Check if the correct answer starts with "a.", "a)", "a " or is just "a"
        # Example correct: "A. Sagittarius A*..."
        is_correct = (
            correct_lower == answer_lower or
            correct_lower.startswith(f"{answer_lower}.") or
            correct_lower.startswith(f"{answer_lower})") or
            correct_lower.startswith(f"{answer_lower} ")
        )
    else:
        # Logic for full text answers
        is_correct = (
            answer_lower == correct_lower or
            # Require significant overlap (at least 5 chars) to prevent "c" matching "black"
            (len(answer_lower) > 4 and answer_lower in correct_lower) or
            # Use 'in' check with length constraint to avoid "c" matching "black holes"
            # But allow "Sagittarius" (11 chars) to match "Sagittarius A*"
            (len(correct_lower) > 4 and correct_lower in answer_lower)
        )
    
    return {
        "solved": is_correct,
        "your_answer": answer,
        "correct_answer": case.correct_answer,
        "explanation": case.explanation,
        "xp_earned": case.xp_reward if is_correct else 25
    }
