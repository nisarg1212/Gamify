"""Gamify AI V2 - Story-Based Learning Platform"""
import os
import uuid
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

# Load environment variables
load_dotenv()

# Import our modules
from gamification import add_xp, get_stats, increment_stat, unlock_achievement
from modules.unified_generator import generate_all_content
from modules.prebuilt_quests import get_all_quest_info
from modules.quiz_mode import score_quiz
from modules.master_mode import score_master
from modules.detective_mode import solve_case
from gamification.models import LearningSession

# Initialize FastAPI
app = FastAPI(title="Gamify AI", description="Transform any topic into a game!")

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
active_sessions = {}

# ==================== Request Models ====================

class TopicRequest(BaseModel):
    topic: str
    api_key: Optional[str] = None

class QuizAnswers(BaseModel):
    answers: List[int]

class MasterAnswers(BaseModel):
    answers: List[str]

class DetectiveAnswer(BaseModel):
    answer: str

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

@app.get("/api/featured-quests")
async def get_featured_quests():
    """Get list of pre-built featured quests"""
    quests = get_all_quest_info()
    return {"quests": quests}

# ==================== Learning Session ====================

@app.post("/api/session/start")
async def start_session(data: TopicRequest):
    """Start a new learning session - generates ALL content at once"""
    session_id = str(uuid.uuid4())[:8]
    
    # Generate ALL content in one API call
    content = generate_all_content(data.topic, user_api_key=data.api_key)
    
    # Check if generation failed
    if content.get("error"):
        return JSONResponse(
            {"error": True, "message": content["message"]}, 
            status_code=503
        )
    
    session = LearningSession(
        session_id=session_id,
        topic=data.topic,
        current_mode="story",
        story=content["story"],
        quiz=content["quiz"],
        master=content["master"],
        detective=content["detective"]
    )
    
    active_sessions[session_id] = session
    
    return {
        "session_id": session_id,
        "topic": data.topic,
        "ai_generated": content.get("success", False),
        "source": content.get("source", "unknown"),
        "story": {
            "title": content["story"].title,
            "content": content["story"].content,
            "xp_reward": content["story"].xp_reward
        }
    }

@app.post("/api/session/{session_id}/complete-story")
async def complete_story(session_id: str):
    """Mark story as complete and return quiz (already generated)"""
    if session_id not in active_sessions:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    
    session = active_sessions[session_id]
    
    if not session.story_completed:
        session.story_completed = True
        add_xp(session.story.xp_reward, "Story completed")
        increment_stat("stories")
        session.total_xp_earned += session.story.xp_reward
    
    session.current_mode = "quiz"
    
    # Quiz was already generated with the session
    return {
        "story_complete": True,
        "xp_earned": session.story.xp_reward,
        "quiz": {
            "questions": [
                {"question": q.question, "options": q.options}
                for q in session.quiz.questions
            ],
            "total_xp": session.quiz.total_xp
        }
    }

@app.post("/api/session/{session_id}/submit-quiz")
async def submit_quiz(session_id: str, data: QuizAnswers):
    """Submit quiz answers and return master practice (already generated)"""
    if session_id not in active_sessions:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    
    session = active_sessions[session_id]
    
    if not session.quiz:
        return JSONResponse({"error": "Quiz not available"}, status_code=400)
    
    result = score_quiz(session.quiz, data.answers)
    
    if not session.quiz_completed:
        session.quiz_completed = True
        add_xp(result["xp_earned"], "Quiz completed")
        increment_stat("quizzes")
        session.total_xp_earned += result["xp_earned"]
        
        if result["percentage"] == 100:
            unlock_achievement("quiz_master")
    
    session.current_mode = "master"
    
    # Master was already generated with the session
    return {
        **result,
        "next_mode": "master",
        "master": {
            "questions": [
                {"question": q.question, "options": q.options}
                for q in session.master.questions
            ],
            "total_xp": session.master.total_xp
        }
    }

@app.post("/api/session/{session_id}/submit-master")
async def submit_master(session_id: str, data: MasterAnswers):
    """Submit master practice answers and return detective case (already generated)"""
    if session_id not in active_sessions:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    
    session = active_sessions[session_id]
    
    if not session.master:
        return JSONResponse({"error": "Master practice not available"}, status_code=400)
    
    result = score_master(session.master, data.answers)
    
    if not session.master_completed:
        session.master_completed = True
        add_xp(result["xp_earned"], "Master practice completed")
        increment_stat("masters")
        session.total_xp_earned += result["xp_earned"]
    
    session.current_mode = "detective"
    
    # Detective was already generated with the session
    return {
        **result,
        "next_mode": "detective",
        "detective": {
            "case_title": session.detective.case_title,
            "scenario": session.detective.scenario,
            "clues": [{"id": c.id, "description": c.description} for c in session.detective.clues],
            "question": session.detective.question,
            "xp_reward": session.detective.xp_reward
        }
    }

@app.post("/api/session/{session_id}/solve-case")
async def solve_detective_case(session_id: str, data: DetectiveAnswer):
    """Submit detective case answer"""
    if session_id not in active_sessions:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    
    session = active_sessions[session_id]
    
    if not session.detective:
        return JSONResponse({"error": "Detective case not available"}, status_code=400)
    
    result = solve_case(session.detective, data.answer)
    
    if not session.detective_completed:
        session.detective_completed = True
        add_xp(result["xp_earned"], "Detective case completed")
        increment_stat("cases")
        session.total_xp_earned += result["xp_earned"]
        
        if result["solved"]:
            unlock_achievement("detective")
    
    return {
        **result,
        "session_complete": True,
        "total_session_xp": session.total_xp_earned
    }

@app.get("/api/session/{session_id}")
async def get_session(session_id: str):
    """Get current session state"""
    if session_id not in active_sessions:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    
    session = active_sessions[session_id]
    return {
        "session_id": session.session_id,
        "topic": session.topic,
        "current_mode": session.current_mode,
        "story_completed": session.story_completed,
        "quiz_completed": session.quiz_completed,
        "master_completed": session.master_completed,
        "detective_completed": session.detective_completed,
        "total_xp_earned": session.total_xp_earned
    }

# ==================== Run ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
