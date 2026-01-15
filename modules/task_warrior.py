"""Task Warrior Module - Turn goals into RPG quests"""
import os
import json
import re
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from gamification.models import Quest, QuestLine

# Load environment variables and configure OpenRouter
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "meta-llama/llama-3.2-3b-instruct:free"

def generate_quests(goal: str, context: str = "") -> QuestLine:
    """Generate RPG-style quests from a goal using OpenRouter"""
    
    prompt = f"""You are an RPG Quest Master. Transform this goal into an epic quest line with smaller quests.

GOAL: {goal}
ADDITIONAL CONTEXT: {context if context else "None provided"}

Create 4-6 quests that break down this goal into achievable steps. Make it feel like an RPG adventure!

Return a JSON object in this EXACT format (no markdown, just pure JSON):
{{
    "goal": "Epic version of the goal",
    "quests": [
        {{
            "id": 1,
            "title": "Quest Name (RPG style)",
            "description": "Quest description with RPG flair (1-2 sentences)",
            "xp_reward": 25,
            "difficulty": "Easy"
        }}
    ],
    "boss_quest": {{
        "id": 99,
        "title": "Final Boss Quest",
        "description": "The ultimate challenge",
        "xp_reward": 100,
        "difficulty": "Epic"
    }}
}}

Difficulty options: Easy, Normal, Hard, Epic
XP rewards: Easy=15, Normal=25, Hard=40, Epic=100
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
        
        quests = [
            Quest(
                id=q["id"],
                title=q["title"],
                description=q["description"],
                xp_reward=q["xp_reward"],
                difficulty=q["difficulty"]
            )
            for q in data["quests"]
        ]
        
        boss = None
        if data.get("boss_quest"):
            boss = Quest(
                id=data["boss_quest"]["id"],
                title=data["boss_quest"]["title"],
                description=data["boss_quest"]["description"],
                xp_reward=data["boss_quest"]["xp_reward"],
                difficulty=data["boss_quest"]["difficulty"]
            )
        
        total_xp = sum(q.xp_reward for q in quests) + (boss.xp_reward if boss else 0)
        
        return QuestLine(
            goal=data["goal"],
            quests=quests,
            total_xp=total_xp,
            boss_quest=boss
        )
    except Exception as e:
        print(f"[QUEST ERROR] {type(e).__name__}: {e}")
        return QuestLine(
            goal=f"⚔️ {goal}",
            quests=[
                Quest(id=1, title="Begin the Journey", description=f"Error: {str(e)[:50]}. Take the first step", xp_reward=15, difficulty="Easy"),
                Quest(id=2, title="Gather Resources", description="Prepare what you need", xp_reward=25, difficulty="Normal"),
                Quest(id=3, title="Face the Challenge", description="Execute your plan", xp_reward=40, difficulty="Hard"),
            ],
            total_xp=180,
            boss_quest=Quest(id=99, title="FINAL: Victory!", description="Complete your goal", xp_reward=100, difficulty="Epic")
        )

def complete_quest(quest_line: QuestLine, quest_id: int) -> dict:
    """Mark a quest as complete and return XP earned"""
    
    for quest in quest_line.quests:
        if quest.id == quest_id and not quest.completed:
            quest.completed = True
            return {
                "quest": quest.title,
                "xp_earned": quest.xp_reward,
                "completed": True,
                "message": f"🎉 Quest Complete: {quest.title}! +{quest.xp_reward} XP"
            }
    
    if quest_line.boss_quest and quest_line.boss_quest.id == quest_id:
        if not quest_line.boss_quest.completed:
            quest_line.boss_quest.completed = True
            return {
                "quest": quest_line.boss_quest.title,
                "xp_earned": quest_line.boss_quest.xp_reward,
                "completed": True,
                "is_boss": True,
                "message": f"🏆 BOSS DEFEATED: {quest_line.boss_quest.title}! +{quest_line.boss_quest.xp_reward} XP"
            }
    
    return {"completed": False, "message": "Quest not found or already completed"}

def get_quest_progress(quest_line: QuestLine) -> dict:
    """Get overall progress on a quest line"""
    completed = sum(1 for q in quest_line.quests if q.completed)
    total = len(quest_line.quests)
    boss_done = quest_line.boss_quest.completed if quest_line.boss_quest else False
    
    xp_earned = sum(q.xp_reward for q in quest_line.quests if q.completed)
    if boss_done and quest_line.boss_quest:
        xp_earned += quest_line.boss_quest.xp_reward
    
    return {
        "completed": completed,
        "total": total,
        "percentage": round((completed / total) * 100, 1) if total > 0 else 0,
        "boss_completed": boss_done,
        "xp_earned": xp_earned,
        "xp_remaining": quest_line.total_xp - xp_earned,
        "all_done": completed == total and boss_done
    }
