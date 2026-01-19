"""SQLAlchemy Database Models"""
from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, default="Player")
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    streak_days = Column(Integer, default=0)
    last_active = Column(String, nullable=True)  # Stored as YYYY-MM-DD
    achievements = Column(JSON, default=list)    # Stored as JSON list of strings
    
    # Stats
    stories_completed = Column(Integer, default=0)
    quizzes_passed = Column(Integer, default=0)
    masters_completed = Column(Integer, default=0)
    cases_solved = Column(Integer, default=0)

class QuestSession(Base):
    """Store active or completed sessions"""
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True)
    topic = Column(String)
    ai_generated = Column(Boolean, default=False)
    created_at = Column(String)  # Timestamp
    completed = Column(Boolean, default=False)
    xp_earned = Column(Integer, default=0)
