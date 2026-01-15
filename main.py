"""Gamify AI - Main FastAPI Application"""
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json

# Load environment variables
load_dotenv()

# Import our modules
from gamification import add_xp, get_stats, increment_stat, unlock_achievement
from modules import (
    generate_quiz, score_quiz,
    generate_quests, complete_quest, get_quest_progress,
    generate_challenge, evaluate_solution, get_challenge_topics
)
from gamification.models import QuestLine

# Initialize FastAPI
app = FastAPI(title="Gamify AI", description="Gamify Everything with AI!")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates
static_path = Path(__file__).parent / "static"
templates_path = Path(__file__).parent / "templates"
static_path.mkdir(exist_ok=True)
templates_path.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)

# In-memory storage for active sessions
active_quizzes = {}
active_quest_lines = {}
active_challenges = {}

# ==================== Request Models ====================

class QuizAnswers(BaseModel):
    answers: List[int]

class GoalRequest(BaseModel):
    goal: str
    context: Optional[str] = ""

class QuestComplete(BaseModel):
    quest_id: int

class ChallengeRequest(BaseModel):
    difficulty: str = "Easy"
    topic: str = "general"

class CodeSubmission(BaseModel):
    code: str

# ==================== Routes ====================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main dashboard"""
    stats = get_stats()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "stats": stats
    })

@app.get("/api/stats")
async def api_stats():
    """Get user gamification stats"""
    return get_stats()

# ==================== Document Quest ====================

@app.post("/api/quiz/generate")
async def api_generate_quiz(content: str = Form(...)):
    """Generate a quiz from text content"""
    quiz = generate_quiz(content)
    quiz_id = hash(quiz.title) % 10000
    active_quizzes[quiz_id] = quiz
    
    return {
        "quiz_id": quiz_id,
        "title": quiz.title,
        "questions": [
            {
                "question": q.question,
                "options": q.options
            }
            for q in quiz.questions
        ],
        "total_xp": quiz.total_xp
    }

@app.post("/api/quiz/{quiz_id}/submit")
async def api_submit_quiz(quiz_id: int, data: QuizAnswers):
    """Submit quiz answers and get results"""
    if quiz_id not in active_quizzes:
        return JSONResponse({"error": "Quiz not found"}, status_code=404)
    
    quiz = active_quizzes[quiz_id]
    result = score_quiz(quiz, data.answers)
    
    # Award XP
    xp_result = add_xp(result["xp_earned"], "Quiz completed")
    increment_stat("quizzes")
    
    if result["perfect"]:
        unlock_achievement("quiz_master")
    
    return {
        **result,
        **xp_result
    }

# ==================== Task Warrior ====================

@app.post("/api/quests/generate")
async def api_generate_quests(data: GoalRequest):
    """Generate quest line from a goal"""
    quest_line = generate_quests(data.goal, data.context)
    quest_id = hash(quest_line.goal) % 10000
    active_quest_lines[quest_id] = quest_line
    
    return {
        "quest_line_id": quest_id,
        "goal": quest_line.goal,
        "quests": [q.model_dump() for q in quest_line.quests],
        "boss_quest": quest_line.boss_quest.model_dump() if quest_line.boss_quest else None,
        "total_xp": quest_line.total_xp
    }

@app.post("/api/quests/{quest_line_id}/complete")
async def api_complete_quest(quest_line_id: int, data: QuestComplete):
    """Mark a quest as complete"""
    if quest_line_id not in active_quest_lines:
        return JSONResponse({"error": "Quest line not found"}, status_code=404)
    
    quest_line = active_quest_lines[quest_line_id]
    result = complete_quest(quest_line, data.quest_id)
    
    if result["completed"]:
        xp_result = add_xp(result["xp_earned"], "Quest completed")
        increment_stat("quests")
        progress = get_quest_progress(quest_line)
        return {**result, **xp_result, "progress": progress}
    
    return result

@app.get("/api/quests/{quest_line_id}/progress")
async def api_quest_progress(quest_line_id: int):
    """Get progress on a quest line"""
    if quest_line_id not in active_quest_lines:
        return JSONResponse({"error": "Quest line not found"}, status_code=404)
    
    return get_quest_progress(active_quest_lines[quest_line_id])

# ==================== Code Arena ====================

@app.get("/api/challenges/topics")
async def api_challenge_topics():
    """Get available challenge topics"""
    return get_challenge_topics()

@app.post("/api/challenges/generate")
async def api_generate_challenge(data: ChallengeRequest):
    """Generate a coding challenge"""
    challenge = generate_challenge(data.difficulty, data.topic)
    active_challenges[challenge.id] = challenge
    
    return {
        "challenge_id": challenge.id,
        "title": challenge.title,
        "description": challenge.description,
        "difficulty": challenge.difficulty,
        "starter_code": challenge.starter_code,
        "hints": challenge.hints,
        "xp_reward": challenge.xp_reward
    }

@app.post("/api/challenges/{challenge_id}/submit")
async def api_submit_challenge(challenge_id: int, data: CodeSubmission):
    """Submit code solution for evaluation"""
    if challenge_id not in active_challenges:
        return JSONResponse({"error": "Challenge not found"}, status_code=404)
    
    challenge = active_challenges[challenge_id]
    result = evaluate_solution(challenge, data.code)
    
    if result.passed:
        total_xp = result.xp_earned + result.bonus_xp
        xp_result = add_xp(total_xp, "Challenge solved")
        increment_stat("challenges")
        return {**result.model_dump(), **xp_result}
    
    return result.model_dump()

# ==================== Run ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
