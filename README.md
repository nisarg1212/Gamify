<p align="center">
  <img src="static/gamify_logo.png" alt="Gamify AI Logo" width="150">
</p>

<h1 align="center">🎮 Gamify AI</h1>

<p align="center">
  <strong>Transform anything into a game. Beat procrastination. Achieve more.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/AI-OpenRouter-purple?style=for-the-badge" alt="AI Powered">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

---

## 🧠 The Problem

In today's hyper-connected world, **distraction is the default**. We're constantly pulled away from meaningful work by notifications, social media, and the endless scroll. Even when we know what we need to do, **procrastination wins** because:

- Tasks feel overwhelming and boring
- There's no immediate reward for progress
- Motivation fades without visible achievements
- Long-term goals feel abstract and distant

**The result?** Unfulfilled potential, abandoned projects, and that nagging feeling of "I should be doing more."

---

## 💡 The Solution: Gamify AI

**Gamify AI** turns any task, learning material, or goal into an engaging game-like experience using artificial intelligence.

We harness the same psychological principles that make games addictive—XP points, levels, achievements, quests, and streaks—and apply them to **real-world productivity**.

> *"What if achieving your goals felt as satisfying as leveling up in a video game?"*

---

## ✨ Features

### 📚 Document Quest
Upload any text or document and transform it into an **interactive quiz**. Learn actively, test your knowledge, and earn XP for correct answers.

- AI-generated questions from any content
- Multiple choice format with explanations
- Perfect score bonuses for mastery

### ⚔️ Task Warrior
Turn your goals into **epic RPG quests**. Break down overwhelming objectives into achievable missions with XP rewards.

- AI transforms goals into quest lines
- Difficulty-based XP rewards (Easy → Epic)
- Boss quests for major milestones
- Progress tracking with visual feedback

### 💻 Code Arena
Challenge yourself with **AI-generated coding problems**. Level up your programming skills through gamified practice.

- Adaptive difficulty (Easy, Medium, Hard)
- Multiple topics (Strings, Arrays, Algorithms, etc.)
- AI-powered code evaluation
- Bonus XP for optimal solutions

### 🏆 Gamification System
A complete RPG-style progression system:

| Feature | Description |
|---------|-------------|
| **XP Points** | Earn experience for every action |
| **Levels** | Level up every 100 XP |
| **Achievements** | 10 unlockable badges |
| **Streaks** | Daily login bonuses |
| **Progress Bar** | Visual XP tracking |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, FastAPI |
| **Frontend** | HTML5, CSS3, JavaScript |
| **AI** | OpenRouter API (Llama 3.2) |
| **Design** | Custom dark theme with glassmorphism |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- OpenRouter API key (free at [openrouter.ai](https://openrouter.ai))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/gamify-ai.git
cd gamify-ai

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with:
OPENROUTER_API_KEY=your_api_key_here

# Run the application
python -m uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) and start gamifying! 🎮

---

## 📁 Project Structure

```
gamify-ai/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not in repo)
├── gamification/
│   ├── engine.py          # XP, levels, achievements
│   └── models.py          # Data models
├── modules/
│   ├── document_quest.py  # Quiz generation
│   ├── task_warrior.py    # Goal → Quest conversion
│   └── code_arena.py      # Coding challenges
├── static/
│   ├── css/style.css      # Modern dark theme
│   └── js/app.js          # Frontend logic
└── templates/
    └── index.html         # Main UI
```

---

## 🔮 Future Vision

**"Gamify anything with a single prompt."**

Our long-term vision is to become the **universal gamification layer** for life:

- 🏃 **Fitness Warrior** - Gamify workout routines
- 💰 **Finance Quest** - Turn saving money into a game
- 📖 **Reading Adventures** - XP for books completed
- 🗣️ **Language Arena** - Gamified language learning
- 🧘 **Habit Dungeons** - RPG-style habit tracking

The possibilities are endless. If humans can do it, Gamify AI can make it fun.

---

## 🎯 Why It Works

Gamification taps into fundamental human psychology:

1. **Dopamine Loops** - Regular XP rewards trigger satisfaction
2. **Loss Aversion** - Streaks motivate daily engagement
3. **Progress Visibility** - Levels provide clear advancement
4. **Achievement Recognition** - Badges validate effort
5. **Chunking** - Quests break big goals into small wins

---

## 🏆 Hackathon Highlights

| Criteria | How We Address It |
|----------|-------------------|
| **Originality** | Novel AI + gamification fusion for productivity |
| **Technical Complexity** | Full-stack app with AI, real-time updates, modular architecture |
| **Problem-Solution Fit** | Directly addresses modern procrastination epidemic |
| **User Experience** | Premium dark theme, smooth animations, intuitive UI |
| **Scalability** | Modular design allows infinite new game modes |

---

## 👥 Team

Built with passion during hackathon 2025 🚀

---

## 📄 License

MIT License - Feel free to use, modify, and distribute.

---

<p align="center">
  <strong>Stop procrastinating. Start playing. Achieve everything.</strong>
</p>

<p align="center">
  Made with 💜 and a lot of ☕
</p>
