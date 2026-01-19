"""Gamification Engine - XP, Levels, Achievements for V2 (SQLite Version)"""
from datetime import datetime
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models_db import Base, User
from .models import UserProgress

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

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

def get_db_user(db: Session) -> User:
    """Get the primary user or create if not exists"""
    user = db.query(User).first()
    if not user:
        user = User(username="Player", xp=0, level=1, achievements=[])
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def get_stats() -> Dict[str, Any]:
    """Get current user stats"""
    db = SessionLocal()
    try:
        user = get_db_user(db)
        return {
            "xp": user.xp,
            "level": calculate_level(user.xp),
            "xp_next": xp_for_next_level(user.xp),
            "streak": user.streak_days,
            "achievements": user.achievements,
            "stats": {
                "stories": user.stories_completed,
                "quizzes": user.quizzes_passed,
                "masters": user.masters_completed,
                "cases": user.cases_solved
            }
        }
    finally:
        db.close()

def unlock_achievement(achievement_id: str) -> bool:
    """Unlock an achievement directly"""
    if achievement_id not in ACHIEVEMENTS:
        return False
        
    db = SessionLocal()
    try:
        user = get_db_user(db)
        
        # Ensure achievements is list
        current_achievements = list(user.achievements) if user.achievements else []
        
        if achievement_id not in current_achievements:
            current_achievements.append(achievement_id)
            user.achievements = current_achievements # Reassign to trigger update
            db.commit()
            return True
        return False
    finally:
        db.close()

def increment_stat(stat_name: str) -> None:
    """Increment a specific stat"""
    db = SessionLocal()
    try:
        user = get_db_user(db)
        # Accept both short and long names
        if stat_name in ["stories_completed", "stories"]:
            user.stories_completed += 1
        elif stat_name in ["quizzes_passed", "quizzes"]:
            user.quizzes_passed += 1
        elif stat_name in ["masters_completed", "masters"]:
            user.masters_completed += 1
        elif stat_name in ["cases_solved", "cases"]:
            user.cases_solved += 1
        db.commit()
    finally:
        db.close()

def add_xp(amount: int, reason: str = "") -> dict:
    """Add XP and check for level ups and achievements"""
    db = SessionLocal()
    try:
        user = get_db_user(db)
        old_level = calculate_level(user.xp)
        
        user.xp += amount
        new_level = calculate_level(user.xp)
        user.level = new_level
        
        # Check streak
        today = datetime.now().strftime("%Y-%m-%d")
        if user.last_active:
            last = datetime.strptime(user.last_active, "%Y-%m-%d")
            diff = (datetime.now() - last).days
            if diff == 1:
                user.streak_days += 1
            elif diff > 1:
                user.streak_days = 1
        else:
            user.streak_days = 1
        user.last_active = today
        
        # Check achievements
        new_achievements = []
        current_achievements = list(user.achievements) if user.achievements else []
        
        # Helper to add achievement
        def try_unlock(aid):
            if aid not in current_achievements:
                current_achievements.append(aid)
                new_achievements.append(ACHIEVEMENTS[aid])
        
        if user.streak_days >= 3: try_unlock("streak_3")
        if user.streak_days >= 7: try_unlock("streak_7")
        if new_level >= 5: try_unlock("level_5")
        if new_level >= 10: try_unlock("level_10")
        
        # Stat-based achievements
        if user.stories_completed >= 1: try_unlock("first_story")
        if user.stories_completed >= 10: try_unlock("storyteller")
        if user.quizzes_passed >= 1: try_unlock("quiz_novice")
        if user.cases_solved >= 1: try_unlock("detective")
        if user.cases_solved >= 5: try_unlock("sherlock")
        
        user.achievements = current_achievements
        db.commit()
        
        leveled_up = new_level > old_level
        
        return {
            "xp_gained": amount,
            "total_xp": user.xp,
            "level": new_level,
            "leveled_up": leveled_up,
            "xp_to_next": xp_for_next_level(user.xp),
            "streak": user.streak_days,
            "new_achievements": new_achievements
        }
    finally:
        db.close()
