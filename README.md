<p align="center">
  <img src="static/gamify_logo.png" alt="Gamify AI Logo" width="150">
</p>

<h1 align="center">🎮 Gamify AI</h1>

<p align="center">
  <strong>Level Up Your Learning. Transform Education into an RPG Adventure.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/AI-OpenRouter-purple?style=for-the-badge" alt="AI Powered">
  <img src="https://img.shields.io/badge/Database-SQLite-yellow?style=for-the-badge&logo=sqlite" alt="SQLite">
</p>

---

## 💡 Inspiration

Traditional learning platforms feel like a chore. We wanted to create an experience where education feels like playing a video game—complete with XP, levels, achievements, and a sense of progression. Inspired by platforms like Duolingo and Codédex, we built **Gamify AI** to make learning addictive.

## 🚀 What It Does

Gamify AI transforms any topic into a 4-stage interactive adventure:

### 1. 📖 Story Mode
Engaging narratives that teach concepts through storytelling rather than dry lectures.

### 2. ❓ Quiz Challenge
Test your comprehension with 5 interactive questions to earn initial XP.

### 3. 🏆 Master Practice
Prove your mastery with advanced application questions that challenge your understanding.

### 4. 🔍 Detective Mode (Special Feature)
A unique mystery-solving mechanic where you must apply what you've learned to solve a case.

---

## ✨ Key Features

- **Hybrid Content System**: 
  - **Featured Quests**: 15 complete learning modules (Python, Black Holes, Dinosaurs, etc.) that work **instantly without API keys**.
  - **Custom Topics**: Generate a full quest on *any* topic using AI (via OpenRouter).
  
- **Leveled Progression**: 
  - Each quest has **3 Difficulty Levels** (Beginner, Intermediate, Advanced).
  - Unlock new levels by proving your skills.

- **RPG Gamification**: 
  - **XP & Levels**: Earn XP for every action, level up your profile.
  - **Achievements**: Unlock badges like "Detective", "Quiz Master", and "Streak Champion".
  - **Streaks**: Daily login rewards to keep you motivated.

- **Retro Aesthetic**: 
  - Beautiful pixel-art UI with dark mode, CRT effects, and 8-bit sounds.

---

## 🛠️ How We Built It

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | Python, FastAPI | High-performance async API handling |
| **Database** | SQLite, SQLAlchemy | Persistent storage for XP, stats, and achievements |
| **AI** | OpenRouter API | Multi-model fallback (Gemini 2.0, Llama 3) for custom topics |
| **Frontend** | Vanilla JS, CSS3 | Custom retro design system without heavy frameworks |
| **Deployment** | Render/Railway | Cloud hosting with gunicorn server |

## 🏆 Accomplishments We're Proud Of

- **Unique Detective Mode**: No other learning platform uses mystery-solving as a core learning mechanic.
- **Robust Hybrid System**: We solved the "AI is slow" problem by having instant pre-built quests while keeping the flexibility of AI generation.
- **Judge-Friendly Flow**: The system intelligently prioritizes server keys and falls back to user keys, ensuring a smooth demo experience.
- **Persistent Progression**: A real database backend means your hard-earned Level 22 status is saved forever.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- (Optional) OpenRouter API Key for custom topics

### Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/gamify-ai.git
cd gamify-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python -m uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) and start your quest! 🎮

### Deployment (Render)

1. **Push to GitHub**
2. **Create Web Service** on Render connected to your repo
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
5. **Env Vars**: Add `OPENROUTER_API_KEY` (optional, for custom topics)

---

## 🔮 What's Next for Gamify AI

- **Multiplayer Arena**: Compete with friends in real-time quiz battles.
- **Classroom Mode**: Teachers can create custom quest paths for students.
- **Mobile App**: Offline mode for on-the-go learning.
- **Shop System**: Spend earned XP on profile customization or power-ups.

---

<p align="center">
  Made during Nexora Hacks 2026
</p>
