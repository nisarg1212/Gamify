/**
 * Gamify AI - Frontend JavaScript
 */

// State
let currentQuiz = null;
let currentQuizId = null;
let currentQuestLine = null;
let currentQuestLineId = null;
let currentChallenge = null;
let currentChallengeId = null;
let selectedDifficulty = 'Easy';
let selectedTopic = 'general';
let userAnswers = [];

// All achievements
const ALL_ACHIEVEMENTS = {
    'first_quiz': { name: 'Quiz Novice', desc: 'Complete your first quiz', icon: '📚' },
    'quiz_master': { name: 'Quiz Master', desc: 'Get 100% on a quiz', icon: '🎓' },
    'quest_starter': { name: 'Quest Starter', desc: 'Complete your first quest', icon: '⚔️' },
    'quest_slayer': { name: 'Quest Slayer', desc: 'Complete 10 quests', icon: '🗡️' },
    'code_warrior': { name: 'Code Warrior', desc: 'Solve your first challenge', icon: '💻' },
    'code_legend': { name: 'Code Legend', desc: 'Solve 10 challenges', icon: '🏆' },
    'streak_3': { name: 'On Fire', desc: '3 day streak', icon: '🔥' },
    'streak_7': { name: 'Unstoppable', desc: '7 day streak', icon: '⚡' },
    'level_5': { name: 'Rising Star', desc: 'Reach level 5', icon: '⭐' },
    'level_10': { name: 'Champion', desc: 'Reach level 10', icon: '👑' }
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadStats();
    renderAchievements([]);
});

// ==================== Stats ====================

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const stats = await response.json();
        updateDisplay(stats);
        renderAchievements(stats.achievements || []);
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

function updateDisplay(stats) {
    document.getElementById('level-badge').textContent = stats.level || 1;
    document.getElementById('xp-current').textContent = stats.xp || 0;
    document.getElementById('xp-next').textContent = `/ ${((stats.level || 1) * 100)} XP`;
    document.getElementById('xp-bar-fill').style.width = `${stats.xp_progress_percent || 0}%`;
    document.getElementById('streak-count').textContent = stats.streak || 0;
    document.getElementById('achievement-count').textContent = 
        (stats.achievements?.length || 0) + '/' + Object.keys(ALL_ACHIEVEMENTS).length;
}

function renderAchievements(unlockedAchievements) {
    const grid = document.getElementById('achievements-grid');
    const unlockedIds = unlockedAchievements.map(a => a.id);
    
    grid.innerHTML = Object.entries(ALL_ACHIEVEMENTS).map(([id, ach]) => `
        <div class="achievement-item ${unlockedIds.includes(id) ? '' : 'locked'}">
            <div class="achievement-icon">${ach.icon}</div>
            <div class="achievement-name">${ach.name}</div>
        </div>
    `).join('');
}

// ==================== Modal Controls ====================

function openModule(moduleName) {
    document.getElementById(`${moduleName}-modal`).classList.add('active');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    // Reset states
    if (modalId === 'document-quest-modal') {
        resetQuiz();
    }
}

// ==================== Document Quest ====================

async function generateQuiz() {
    const content = document.getElementById('document-content').value.trim();
    if (!content) {
        alert('Please paste some text content first!');
        return;
    }

    const btn = document.getElementById('generate-quiz-btn');
    btn.innerHTML = '<span class="spinner"></span> Generating...';
    btn.disabled = true;

    try {
        const formData = new FormData();
        formData.append('content', content);

        const response = await fetch('/api/quiz/generate', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        currentQuiz = data;
        currentQuizId = data.quiz_id;
        userAnswers = new Array(data.questions.length).fill(-1);
        
        renderQuiz(data);
        document.getElementById('quiz-input-section').style.display = 'none';
        document.getElementById('quiz-section').style.display = 'block';
    } catch (error) {
        console.error('Error generating quiz:', error);
        alert('Failed to generate quiz. Please try again.');
    } finally {
        btn.innerHTML = '<span>✨</span> Generate Quiz';
        btn.disabled = false;
    }
}

function renderQuiz(quiz) {
    const section = document.getElementById('quiz-section');
    section.innerHTML = `
        <h3 style="margin-bottom: 20px; color: var(--accent-primary);">📝 ${quiz.title}</h3>
        <p style="color: var(--text-secondary); margin-bottom: 24px;">
            Answer all questions to earn up to <strong>${quiz.total_xp} XP</strong>!
        </p>
        ${quiz.questions.map((q, i) => `
            <div class="quiz-question">
                <div class="question-number">Question ${i + 1} of ${quiz.questions.length}</div>
                <div class="question-text">${q.question}</div>
                <div class="options-list">
                    ${q.options.map((opt, j) => `
                        <div class="option-item" onclick="selectAnswer(${i}, ${j}, this)" data-q="${i}" data-a="${j}">
                            <span class="option-letter">${String.fromCharCode(65 + j)}</span>
                            <span>${opt}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `).join('')}
        <button class="btn btn-primary" onclick="submitQuiz()" style="width: 100%; margin-top: 16px;">
            <span>✅</span> Submit Answers
        </button>
    `;
}

function selectAnswer(questionIndex, answerIndex, element) {
    userAnswers[questionIndex] = answerIndex;
    
    // Update UI
    document.querySelectorAll(`[data-q="${questionIndex}"]`).forEach(opt => {
        opt.classList.remove('selected');
    });
    element.classList.add('selected');
}

async function submitQuiz() {
    if (userAnswers.includes(-1)) {
        alert('Please answer all questions!');
        return;
    }

    try {
        const response = await fetch(`/api/quiz/${currentQuizId}/submit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answers: userAnswers })
        });

        const result = await response.json();
        showQuizResults(result);
        
        // Show XP animation
        showXPPopup(result.xp_gained);
        if (result.leveled_up) {
            showLevelUp(result.level);
        }
        
        // Refresh stats
        loadStats();
    } catch (error) {
        console.error('Error submitting quiz:', error);
    }
}

function showQuizResults(result) {
    document.getElementById('quiz-section').style.display = 'none';
    const resultsDiv = document.getElementById('quiz-results');
    resultsDiv.style.display = 'block';
    
    const emoji = result.percentage >= 80 ? '🎉' : result.percentage >= 50 ? '👍' : '📚';
    
    resultsDiv.innerHTML = `
        <div class="result-card">
            <div class="result-icon">${emoji}</div>
            <div class="result-title">
                ${result.perfect ? '🌟 Perfect Score! 🌟' : `${result.correct}/${result.total} Correct`}
            </div>
            <div class="result-xp">+${result.xp_earned} XP</div>
            ${result.bonus_xp > 0 ? `<p style="color: var(--success);">Bonus: +${result.bonus_xp} XP</p>` : ''}
            <p style="color: var(--text-secondary); margin: 16px 0;">
                You scored ${result.percentage}%
            </p>
            <button class="btn btn-primary" onclick="resetQuiz()">
                <span>🔄</span> Try Another Quiz
            </button>
        </div>
        
        <h4 style="margin-top: 32px; margin-bottom: 16px;">📋 Review Answers</h4>
        ${result.results.map((r, i) => `
            <div class="quiz-question" style="border-left: 4px solid ${r.is_correct ? 'var(--success)' : 'var(--danger)'};">
                <div class="question-text" style="margin-bottom: 8px;">${r.question}</div>
                <p style="color: ${r.is_correct ? 'var(--success)' : 'var(--danger)'};">
                    ${r.is_correct ? '✅' : '❌'} Your answer: ${r.your_answer}
                </p>
                ${!r.is_correct ? `<p style="color: var(--success);">✓ Correct: ${r.correct_answer}</p>` : ''}
                <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 8px;">
                    💡 ${r.explanation}
                </p>
            </div>
        `).join('')}
    `;
}

function resetQuiz() {
    document.getElementById('quiz-input-section').style.display = 'block';
    document.getElementById('quiz-section').style.display = 'none';
    document.getElementById('quiz-results').style.display = 'none';
    document.getElementById('document-content').value = '';
    currentQuiz = null;
    currentQuizId = null;
    userAnswers = [];
}

// ==================== Task Warrior ====================

async function generateQuests() {
    const goal = document.getElementById('goal-input').value.trim();
    if (!goal) {
        alert('Please enter a goal!');
        return;
    }

    const context = document.getElementById('goal-context').value.trim();
    const btn = document.getElementById('generate-quests-btn');
    btn.innerHTML = '<span class="spinner"></span> Creating Quest Line...';
    btn.disabled = true;

    try {
        const response = await fetch('/api/quests/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ goal, context })
        });

        const data = await response.json();
        currentQuestLine = data;
        currentQuestLineId = data.quest_line_id;
        
        renderQuests(data);
        document.getElementById('quest-input-section').style.display = 'none';
        document.getElementById('quest-section').style.display = 'block';
    } catch (error) {
        console.error('Error generating quests:', error);
        alert('Failed to create quest line. Please try again.');
    } finally {
        btn.innerHTML = '<span>⚔️</span> Create Quest Line';
        btn.disabled = false;
    }
}

function renderQuests(data) {
    const section = document.getElementById('quest-section');
    section.innerHTML = `
        <h3 style="margin-bottom: 8px; color: var(--accent-primary);">⚔️ ${data.goal}</h3>
        <p style="color: var(--text-secondary); margin-bottom: 24px;">
            Complete all quests to earn <strong>${data.total_xp} XP</strong>!
        </p>
        
        <div id="quests-list">
            ${data.quests.map(q => renderQuestItem(q)).join('')}
        </div>
        
        ${data.boss_quest ? `
            <h4 style="margin-top: 24px; margin-bottom: 12px; color: #a855f7;">👹 BOSS QUEST</h4>
            ${renderQuestItem(data.boss_quest, true)}
        ` : ''}
        
        <button class="btn btn-secondary" onclick="resetQuests()" style="width: 100%; margin-top: 24px;">
            <span>🔄</span> New Quest Line
        </button>
    `;
}

function renderQuestItem(quest, isBoss = false) {
    const diffClass = quest.difficulty.toLowerCase();
    return `
        <div class="quest-item ${quest.completed ? 'completed' : ''}" id="quest-${quest.id}">
            <div class="quest-checkbox ${quest.completed ? 'checked' : ''}" 
                 onclick="completeQuest(${quest.id})"
                 ${quest.completed ? 'style="pointer-events: none;"' : ''}>
                ${quest.completed ? '✓' : ''}
            </div>
            <div class="quest-content">
                <div class="quest-title">${isBoss ? '👹 ' : ''}${quest.title}</div>
                <div class="quest-description">${quest.description}</div>
            </div>
            <span class="quest-difficulty difficulty-${diffClass}">${quest.difficulty}</span>
            <span class="quest-xp">+${quest.xp_reward} XP</span>
        </div>
    `;
}

async function completeQuest(questId) {
    try {
        const response = await fetch(`/api/quests/${currentQuestLineId}/complete`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ quest_id: questId })
        });

        const result = await response.json();
        
        if (result.completed) {
            // Update UI
            const questEl = document.getElementById(`quest-${questId}`);
            questEl.classList.add('completed');
            const checkbox = questEl.querySelector('.quest-checkbox');
            checkbox.classList.add('checked');
            checkbox.innerHTML = '✓';
            checkbox.style.pointerEvents = 'none';
            
            // Show XP animation
            showXPPopup(result.xp_earned);
            if (result.leveled_up) {
                showLevelUp(result.level);
            }
            
            // Refresh stats
            loadStats();
        }
    } catch (error) {
        console.error('Error completing quest:', error);
    }
}

function resetQuests() {
    document.getElementById('quest-input-section').style.display = 'block';
    document.getElementById('quest-section').style.display = 'none';
    document.getElementById('goal-input').value = '';
    document.getElementById('goal-context').value = '';
    currentQuestLine = null;
    currentQuestLineId = null;
}

// ==================== Code Arena ====================

function selectDifficulty(diff, btn) {
    selectedDifficulty = diff;
    document.querySelectorAll('.difficulty-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}

function selectTopic(topic, btn) {
    selectedTopic = topic;
    document.querySelectorAll('.topic-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}

async function generateChallenge() {
    const btn = document.getElementById('generate-challenge-btn');
    btn.innerHTML = '<span class="spinner"></span> Generating Challenge...';
    btn.disabled = true;

    try {
        const response = await fetch('/api/challenges/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ difficulty: selectedDifficulty, topic: selectedTopic })
        });

        const data = await response.json();
        currentChallenge = data;
        currentChallengeId = data.challenge_id;
        
        renderChallenge(data);
        document.getElementById('challenge-select-section').style.display = 'none';
        document.getElementById('challenge-section').style.display = 'block';
    } catch (error) {
        console.error('Error generating challenge:', error);
        alert('Failed to generate challenge. Please try again.');
    } finally {
        btn.innerHTML = '<span>⚡</span> Start Challenge';
        btn.disabled = false;
    }
}

function renderChallenge(challenge) {
    const section = document.getElementById('challenge-section');
    section.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <h3 style="color: var(--accent-primary);">${challenge.title}</h3>
            <span class="quest-difficulty difficulty-${challenge.difficulty.toLowerCase()}">${challenge.difficulty}</span>
        </div>
        
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
            ${challenge.description}
        </p>
        
        <p style="color: var(--accent-primary); margin-bottom: 24px;">
            🎯 Reward: <strong>+${challenge.xp_reward} XP</strong> (bonus for optimal solution!)
        </p>
        
        <div class="code-editor">
            <div class="code-editor-header">
                <span class="dot dot-red"></span>
                <span class="dot dot-yellow"></span>
                <span class="dot dot-green"></span>
                <span style="margin-left: 12px;">solution.py</span>
            </div>
            <textarea class="code-textarea" id="code-input">${challenge.starter_code}</textarea>
        </div>
        
        <div class="hints-container">
            <h4 style="margin-bottom: 12px;">💡 Hints</h4>
            ${challenge.hints.map((hint, i) => `
                <div class="hint-item">
                    <span class="hint-icon">💡</span>
                    <span>${hint}</span>
                </div>
            `).join('')}
        </div>
        
        <div style="display: flex; gap: 12px; margin-top: 24px;">
            <button class="btn btn-primary" onclick="submitCode()" style="flex: 1;">
                <span>🚀</span> Submit Solution
            </button>
            <button class="btn btn-secondary" onclick="resetChallenge()">
                <span>🔄</span> New Challenge
            </button>
        </div>
        
        <div id="challenge-result" style="margin-top: 24px;"></div>
    `;
}

async function submitCode() {
    const code = document.getElementById('code-input').value;
    
    try {
        const response = await fetch(`/api/challenges/${currentChallengeId}/submit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code })
        });

        const result = await response.json();
        showChallengeResult(result);
        
        if (result.passed) {
            showXPPopup(result.xp_earned + (result.bonus_xp || 0));
            if (result.leveled_up) {
                showLevelUp(result.level);
            }
            loadStats();
        }
    } catch (error) {
        console.error('Error submitting code:', error);
    }
}

function showChallengeResult(result) {
    const resultDiv = document.getElementById('challenge-result');
    const icon = result.passed ? '✅' : '❌';
    const bgColor = result.passed ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)';
    const borderColor = result.passed ? 'var(--success)' : 'var(--danger)';
    
    resultDiv.innerHTML = `
        <div style="background: ${bgColor}; border: 1px solid ${borderColor}; border-radius: var(--radius-lg); padding: 24px;">
            <h4 style="margin-bottom: 12px;">${icon} ${result.passed ? 'Challenge Complete!' : 'Not Quite Right'}</h4>
            <p style="color: var(--text-secondary);">${result.feedback}</p>
            ${result.passed ? `
                <p style="color: var(--success); margin-top: 12px; font-weight: 600;">
                    +${result.xp_earned} XP earned!
                    ${result.bonus_xp > 0 ? `(+${result.bonus_xp} bonus!)` : ''}
                </p>
            ` : ''}
        </div>
    `;
}

function resetChallenge() {
    document.getElementById('challenge-select-section').style.display = 'block';
    document.getElementById('challenge-section').style.display = 'none';
    currentChallenge = null;
    currentChallengeId = null;
}

// ==================== Animations ====================

function showXPPopup(xp) {
    const popup = document.getElementById('xp-popup');
    document.getElementById('xp-popup-value').textContent = `+${xp} XP`;
    popup.style.display = 'block';
    
    setTimeout(() => {
        popup.style.display = 'none';
    }, 2000);
}

function showLevelUp(level) {
    const overlay = document.getElementById('level-up-overlay');
    document.getElementById('new-level').textContent = level;
    overlay.classList.add('active');
    
    setTimeout(() => {
        overlay.classList.remove('active');
    }, 3000);
}

// Close modals on overlay click
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            overlay.classList.remove('active');
        }
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
    }
});
