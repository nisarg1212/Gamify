"""Unified Learning Generator - Hybrid content with multi-model fallback"""
import os
import json
import re
import time
import httpx
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import Story, Quiz, QuizQuestion, MasterPractice, MasterQuestion, DetectiveCase, Clue
from modules.prebuilt_quests import is_featured_quest, get_featured_quest

# Load environment variables and configure OpenRouter with LONG timeout
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    timeout=httpx.Timeout(60.0, connect=10.0)  # 60 second timeout, 10 second connect
)

# Models to try in order (free tier - Jan 2026)
MODELS = [
    "google/gemini-2.0-flash-exp:free",
    "google/gemma-3-27b-it:free",
    "meta-llama/llama-3.3-70b-instruct:free",
]

def generate_all_content(topic: str, user_api_key: str = None) -> dict:
    """Generate all learning content - uses pre-built quests or AI with fallback"""
    
    # Check if this matches a featured quest
    featured_match = is_featured_quest(topic)
    if featured_match:
        quest_id, level = featured_match
        print(f"[HYBRID] Using pre-built quest: {quest_id} (Level {level})")
        quest = get_featured_quest(quest_id, level)
        return {
            "success": True,
            "source": f"prebuilt (Level {level})",
            "story": quest["story"],
            "quiz": quest["quiz"],
            "master": quest["master"],
            "detective": quest["detective"]
        }
    
    # Try AI generation with multiple models
    return generate_with_fallback(topic, user_api_key)


def get_client(user_api_key: str = None):
    """Get OpenAI client - tries server key first, then user key"""
    # Try server key first (for judges), then user key as fallback
    server_key = os.getenv("OPENROUTER_API_KEY")
    api_key = server_key or user_api_key
    
    if not api_key:
        return None
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        timeout=httpx.Timeout(60.0, connect=10.0)
    )


def generate_with_fallback(topic: str, user_api_key: str = None) -> dict:
    """Try multiple models, fall back if one fails"""
    
    prompt = f"""Create a complete learning experience about: {topic}

Generate ALL of the following in ONE JSON response:

1. STORY: An engaging educational narrative (200-300 words)
2. QUIZ: 5 basic comprehension questions
3. MASTER: 3 advanced application questions  
4. DETECTIVE: A mystery case to solve

Return ONLY valid JSON in this exact format:
{{
  "story": {{
    "title": "Engaging story title",
    "content": "Full story text here...",
    "key_facts": ["fact1", "fact2", "fact3", "fact4", "fact5"]
  }},
  "quiz": {{
    "questions": [
      {{"question": "Q?", "options": ["A","B","C","D"], "correct_index": 0, "explanation": "Why"}}
    ]
  }},
  "master": {{
    "questions": [
      {{"question": "Advanced Q?", "options": ["A","B","C","D"], "correct_answer": "A", "explanation": "Why"}}
    ]
  }},
  "detective": {{
    "case_title": "Mystery Title",
    "scenario": "Mystery setup (2-3 sentences)",
    "clues": [{{"id": 1, "description": "Clue text"}}],
    "question": "What is the answer?",
    "options": ["A","B","C","D"],
    "correct_answer": "A",
    "explanation": "Why this is correct"
  }}
}}"""

    # Get client with user or server API key
    api_client = get_client(user_api_key)
    if not api_client:
        return {
            "error": True,
            "message": "No API key available. Please enter your OpenRouter API key for custom topics, or try a Featured Quest!"
        }

    for i, model in enumerate(MODELS):
        try:
            print(f"[AI] Trying model {i+1}/{len(MODELS)}: {model}")
            
            response = api_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=3000
            )
            
            if not response or not response.choices:
                print(f"[AI] Model {model} returned empty response")
                continue
            
            text = response.choices[0].message.content
            if not text:
                continue
            
            # Parse the response
            result = parse_ai_response(text, topic)
            if result:
                print(f"[AI] Success with model: {model}")
                return result
                
        except httpx.TimeoutException:
            print(f"[AI] Model {model} timed out (60s)")
            continue
        except Exception as e:
            print(f"[AI] Model {model} failed: {type(e).__name__}: {e}")
            continue
    
    # All models failed, return friendly error
    print(f"[AI] All models failed for: {topic}")
    return {
        "error": True,
        "message": "AI generation unavailable. Please try one of our Featured Quests instead! 🎮"
    }



def parse_ai_response(text: str, topic: str) -> dict | None:
    """Parse AI response into structured content"""
    try:
        text = text.strip()
        
        # Remove markdown code blocks
        if "```" in text:
            text = re.sub(r'```json?\s*', '', text)
            text = re.sub(r'```', '', text)
        
        # Extract JSON with improved regex to handle multiple braces or extra text
        # Finds the first '{' and the last '}'
        start_idx = text.find('{')
        end_idx = text.rfind('}')
        
        if start_idx != -1 and end_idx != -1:
            text = text[start_idx:end_idx+1]

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            # Fallback: try to clean common issues like trailing commas
            text = re.sub(r',\s*}', '}', text)
            text = re.sub(r',\s*]', ']', text)
            data = json.loads(text)
        
        # Parse Story
        story_data = data.get("story", {})
        story = Story(
            topic=topic,
            title=story_data.get("title", f"Learning About {topic}"),
            content=story_data.get("content", f"An amazing journey into {topic}..."),
            key_facts=story_data.get("key_facts", [f"{topic} is fascinating"])[:5],
            xp_reward=15
        )
        
        # Parse Quiz
        quiz_data = data.get("quiz", {})
        quiz_questions = []
        for q in quiz_data.get("questions", [])[:5]:
            quiz_questions.append(QuizQuestion(
                question=q.get("question", "Question"),
                options=q.get("options", ["A", "B", "C", "D"]),
                correct_index=q.get("correct_index", 0),
                explanation=q.get("explanation", "Correct!")
            ))
        
        if not quiz_questions:
            return None  # Invalid response, try next model
        
        quiz = Quiz(
            topic=topic,
            questions=quiz_questions,
            difficulty="basic",
            total_xp=len(quiz_questions) * 10 + 20
        )
        
        # Parse Master
        master_data = data.get("master", {})
        master_questions = []
        for q in master_data.get("questions", [])[:3]:
            master_questions.append(MasterQuestion(
                question=q.get("question", "Advanced question"),
                question_type="multiple_choice",
                options=q.get("options", ["A", "B", "C", "D"]),
                correct_answer=q.get("correct_answer", "A"),
                explanation=q.get("explanation", "Correct!"),
                xp_reward=20
            ))
        
        if not master_questions:
            return None
        
        master = MasterPractice(
            topic=topic,
            questions=master_questions,
            total_xp=len(master_questions) * 20 + 50
        )
        
        # Parse Detective
        det_data = data.get("detective", {})
        clues = [Clue(id=c.get("id", i+1), description=c.get("description", "Clue"), is_key_clue=True) 
                 for i, c in enumerate(det_data.get("clues", [])[:4])]
        
        if not clues:
            return None
        
        options = det_data.get("options", [])
        question = det_data.get("question", "Solve the mystery")
        if options:
            question += "\n\n" + "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(options[:4])])
        
        detective = DetectiveCase(
            topic=topic,
            case_title=det_data.get("case_title", f"The {topic} Mystery"),
            scenario=det_data.get("scenario", f"A mystery about {topic} awaits..."),
            clues=clues,
            question=question,
            correct_answer=det_data.get("correct_answer", "A"),
            explanation=det_data.get("explanation", "Great detective work!"),
            xp_reward=100
        )
        
        return {
            "success": True,
            "source": "ai",
            "story": story,
            "quiz": quiz,
            "master": master,
            "detective": detective
        }
        
    except Exception as e:
        print(f"[PARSE] Error: {type(e).__name__}: {e}")
        return None


def generate_smart_fallback(topic: str) -> dict:
    """Return error when AI fails - prompt user to try featured quests"""
    return {
        "success": False,
        "error": True,
        "message": f"Unable to generate content for '{topic}'. Please try one of our Featured Quests, or try again later!",
        "source": "error"
    }

