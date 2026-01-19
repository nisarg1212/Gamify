"""Data models for Gamify AI V2 - Story-Based Learning"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ==================== User Progress ====================

class UserProgress(BaseModel):
    """Track user's gamification progress"""
    xp: int = 0
    level: int = 1
    streak_days: int = 0
    last_active: Optional[str] = None
    achievements: List[str] = []
    stories_completed: int = 0
    quizzes_passed: int = 0
    masters_completed: int = 0
    cases_solved: int = 0

# ==================== Story Mode ====================

class Story(BaseModel):
    """Generated story from a topic"""
    topic: str
    title: str
    content: str  # The full story text
    key_facts: List[str]  # Extracted facts for quiz generation
    xp_reward: int = 15

# ==================== Quiz Mode ====================

class QuizQuestion(BaseModel):
    """A single quiz question"""
    question: str
    options: List[str]
    correct_index: int
    explanation: str

class Quiz(BaseModel):
    """Quick test quiz"""
    topic: str
    questions: List[QuizQuestion]
    difficulty: str = "basic"  # basic, advanced
    total_xp: int = 50

# ==================== Master Mode ====================

class MasterQuestion(BaseModel):
    """Advanced master practice question"""
    question: str
    question_type: str  # multiple_choice, short_answer, application
    options: Optional[List[str]] = None
    correct_answer: str
    explanation: str
    xp_reward: int = 20

class MasterPractice(BaseModel):
    """Master practice session"""
    topic: str
    questions: List[MasterQuestion]
    total_xp: int = 100

# ==================== Detective Mode ====================

class Clue(BaseModel):
    """A clue in the detective case"""
    id: int
    description: str
    is_key_clue: bool = False

class DetectiveCase(BaseModel):
    """Mystery case to solve"""
    topic: str
    case_title: str
    scenario: str  # The mystery setup
    clues: List[Clue]
    question: str  # What needs to be solved
    correct_answer: str
    explanation: str
    xp_reward: int = 100

# ==================== Learning Session ====================

class LearningSession(BaseModel):
    """Complete learning session state"""
    session_id: str
    topic: str
    current_mode: str  # story, quiz, master, detective
    story: Optional[Story] = None
    quiz: Optional[Quiz] = None
    master: Optional[MasterPractice] = None
    detective: Optional[DetectiveCase] = None
    story_completed: bool = False
    quiz_completed: bool = False
    master_completed: bool = False
    detective_completed: bool = False
    total_xp_earned: int = 0
