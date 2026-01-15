"""Data models for Gamify AI"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserProgress(BaseModel):
    """Track user's gamification progress"""
    xp: int = 0
    level: int = 1
    streak_days: int = 0
    last_active: Optional[str] = None
    achievements: List[str] = []
    quests_completed: int = 0
    challenges_solved: int = 0
    quizzes_taken: int = 0

class QuizQuestion(BaseModel):
    """A single quiz question"""
    question: str
    options: List[str]
    correct_index: int
    explanation: str

class Quiz(BaseModel):
    """Generated quiz from document"""
    title: str
    questions: List[QuizQuestion]
    total_xp: int = 50

class Quest(BaseModel):
    """A task broken into RPG-style quest"""
    id: int
    title: str
    description: str
    xp_reward: int
    completed: bool = False
    difficulty: str = "Normal"  # Easy, Normal, Hard, Epic

class QuestLine(BaseModel):
    """Collection of quests for a goal"""
    goal: str
    quests: List[Quest]
    total_xp: int
    boss_quest: Optional[Quest] = None

class CodeChallenge(BaseModel):
    """A coding challenge"""
    id: int
    title: str
    description: str
    difficulty: str  # Easy, Medium, Hard
    starter_code: str
    test_cases: List[str]
    hints: List[str]
    xp_reward: int

class ChallengeResult(BaseModel):
    """Result of code challenge submission"""
    passed: bool
    feedback: str
    xp_earned: int
    bonus_xp: int = 0
