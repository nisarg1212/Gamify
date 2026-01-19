"""Gamification Engine - XP, Levels, Achievements for V2"""
import json
from datetime import datetime
from pathlib import Path
from typing import Optional
from .models import UserProgress

DATA_FILE = Path(__file__).parent.parent / "data" / "user_progress.json"

# Achievement definitions for V2
ACHIEVEMENTS = {
    "first_story": {"name": "Story Seeker", "desc": "Complete your first story", "icon": "📖"},
    "storyteller": {"name": "Storyteller", "desc": "Complete 10 stories", "icon": "📚"},
    "quiz_novice": {"name": "Quiz Novice", "desc": "Pass your first quiz", "icon": "❓"},
    "quiz_master": {"name": "Quiz Master", "desc": "Get 100% on a quiz", "icon": "🎓"},
    "master_student": {"name": "Master Student", "desc": "Complete master practice", "icon": "🏆"},
    "detective": {"name": "Detective", "desc": "Solve your first case", "icon": "🔍"},
    "sherlock": {"name": "Sherlock", "desc": "Solve 5 cases", "icon": "🕵️"},
    "streak_3": {"name": "On Fire", "desc": "3 day streak", "icon": "🔥"},
    "streak_7": {"name": "Unstoppable", "desc": "7 day streak", "icon": "⚡"},
    "level_5": {"name": "Rising Star", "desc": "Reach level 5", "icon": "⭐"},
    "level_10": {"name": "Champion", "desc": "Reach level 10", "icon": "👑"},
}

def calculate_level(xp: int) -> int:
    """Calculate level from XP (100 XP per level)"""
    return (xp // 100) + 1

def xp_for_next_level(current_xp: int) -> int:
    """XP needed for next level"""
    current_level = calculate_level(current_xp)
    return (current_level * 100) - current_xp

def load_progress() -> UserProgress:
    """Load user progress from file"""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return UserProgress(**data)
    return UserProgress()

def save_progress(progress: UserProgress) -> None:
    """Save user progress to file"""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(progress.model_dump(), f, indent=2)

def add_xp(amount: int, reason: str = "") -> dict:
    """Add XP and check for level ups and achievements"""
    progress = load_progress()
    old_level = progress.level
    
    progress.xp += amount
    progress.level = calculate_level(progress.xp)
    
    # Check streak
    today = datetime.now().strftime("%Y-%m-%d")
    if progress.last_active:
        last = datetime.strptime(progress.last_active, "%Y-%m-%d")
        diff = (datetime.now() - last).days
        if diff == 1:
            progress.streak_days += 1
        elif diff > 1:
            progress.streak_days = 1
    else:
        progress.streak_days = 1
    progress.last_active = today
    
    # Check achievements
    new_achievements = []
    
    if progress.streak_days >= 3 and "streak_3" not in progress.achievements:
        progress.achievements.append("streak_3")
        new_achievements.append(ACHIEVEMENTS["streak_3"])
    
    if progress.streak_days >= 7 and "streak_7" not in progress.achievements:
        progress.achievements.append("streak_7")
        new_achievements.append(ACHIEVEMENTS["streak_7"])
    
    if progress.level >= 5 and "level_5" not in progress.achievements:
        progress.achievements.append("level_5")
        new_achievements.append(ACHIEVEMENTS["level_5"])
    
    if progress.level >= 10 and "level_10" not in progress.achievements:
        progress.achievements.append("level_10")
        new_achievements.append(ACHIEVEMENTS["level_10"])
    
    save_progress(progress)
    
    leveled_up = progress.level > old_level
    
    return {
        "xp_gained": amount,
        "total_xp": progress.xp,
        "level": progress.level,
        "leveled_up": leveled_up,
        "xp_to_next": xp_for_next_level(progress.xp),
        "streak": progress.streak_days,
        "new_achievements": new_achievements
    }

def unlock_achievement(achievement_id: str) -> Optional[dict]:
    """Unlock a specific achievement"""
    if achievement_id not in ACHIEVEMENTS:
        return None
    
    progress = load_progress()
    if achievement_id in progress.achievements:
        return None
    
    progress.achievements.append(achievement_id)
    save_progress(progress)
    
    return ACHIEVEMENTS[achievement_id]

def get_stats() -> dict:
    """Get current user stats for dashboard"""
    progress = load_progress()
    
    return {
        "xp": progress.xp,
        "level": progress.level,
        "xp_to_next": xp_for_next_level(progress.xp),
        "xp_progress_percent": ((progress.xp % 100) / 100) * 100,
        "streak": progress.streak_days,
        "achievements": [
            {**ACHIEVEMENTS[a], "id": a} 
            for a in progress.achievements 
            if a in ACHIEVEMENTS
        ],
        "total_achievements": len(ACHIEVEMENTS),
        "stories_completed": progress.stories_completed,
        "quizzes_passed": progress.quizzes_passed,
        "masters_completed": progress.masters_completed,
        "cases_solved": progress.cases_solved
    }

def increment_stat(stat: str) -> None:
    """Increment a specific stat counter"""
    progress = load_progress()
    
    if stat == "stories":
        progress.stories_completed += 1
        if progress.stories_completed == 1:
            unlock_achievement("first_story")
        elif progress.stories_completed >= 10:
            unlock_achievement("storyteller")
    elif stat == "quizzes":
        progress.quizzes_passed += 1
        if progress.quizzes_passed == 1:
            unlock_achievement("quiz_novice")
    elif stat == "masters":
        progress.masters_completed += 1
        if progress.masters_completed == 1:
            unlock_achievement("master_student")
    elif stat == "cases":
        progress.cases_solved += 1
        if progress.cases_solved == 1:
            unlock_achievement("detective")
        elif progress.cases_solved >= 5:
            unlock_achievement("sherlock")
    
    save_progress(progress)
