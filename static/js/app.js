/**
 * Gamify AI V2 - Story-Based Learning Frontend (Unified API Version)
 */

// Session state
let currentSession = null;
let currentLevel = 1;
let maxLevel = 3;
let selectedQuizAnswers = [];
let selectedMasterAnswers = [];
let ttsUtterance = null;
let isSpeaking = false;

// All achievements
const ALL_ACHIEVEMENTS = {
    "first_story": { name: "Story Seeker", desc: "Complete your first story", icon: "📖" },
    "storyteller": { name: "Storyteller", desc: "Complete 10 stories", icon: "📚" },
    "quiz_novice": { name: "Quiz Novice", desc: "Pass your first quiz", icon: "❓" },
    "quiz_master": { name: "Quiz Master", desc: "Get 100% on a quiz", icon: "🎓" },
    "master_student": { name: "Master Student", desc: "Complete master practice", icon: "🏆" },
    "detective": { name: "Detective", desc: "Solve your first case", icon: "🔍" },
    "sherlock": { name: "Sherlock", desc: "Solve 5 cases", icon: "🕵️" },
    "streak_3": { name: "On Fire", desc: "3 day streak", icon: "🔥" },
    "streak_7": { name: "Unstoppable", desc: "7 day streak", icon: "⚡" },
    "level_5": { name: "Rising Star", desc: "Reach level 5", icon: "⭐" },
    "level_10": { name: "Champion", desc: "Reach level 10", icon: "👑" }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadStats();
    loadFeaturedQuests();
    renderAchievements([]);
    loadApiKey();

    // Enter key to start
    document.getElementById('topic-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') startLearning();
    });
});

// ==================== API Key Management ====================

function toggleApiKeySection() {
    const container = document.getElementById('api-key-container');
    const arrow = document.getElementById('api-key-arrow');
    if (container.style.display === 'none') {
        container.style.display = 'block';
        arrow.style.transform = 'rotate(90deg)';
    } else {
        container.style.display = 'none';
        arrow.style.transform = 'rotate(0deg)';
    }
}

function saveApiKey() {
    const apiKey = document.getElementById('api-key-input').value.trim();
    if (apiKey) {
        localStorage.setItem('openrouter_api_key', apiKey);
        const status = document.getElementById('api-key-status');
        status.textContent = '✓ API key saved!';
        status.className = 'api-key-status saved';
        setTimeout(() => { status.textContent = ''; }, 2000);
    }
}

function loadApiKey() {
    const savedKey = localStorage.getItem('openrouter_api_key');
    if (savedKey) {
        document.getElementById('api-key-input').value = savedKey;
    }
}

function getUserApiKey() {
    return localStorage.getItem('openrouter_api_key') || '';
}

function toggleKeyVisibility() {
    const input = document.getElementById('api-key-input');
    input.type = input.type === 'password' ? 'text' : 'password';
}

// Activate a progress step in the sidebar
function activateStep(stepName) {
    // Remove all active classes
    document.querySelectorAll('.progress-step-v').forEach(step => {
        step.classList.remove('active');
    });

    // Add active class to current step
    const currentStep = document.getElementById(`step-${stepName}`);
    if (currentStep) {
        currentStep.classList.add('active');
    }

    // Mark previous steps as completed
    const stepOrder = ['story', 'quiz', 'master', 'detective'];
    const currentIndex = stepOrder.indexOf(stepName);
    stepOrder.forEach((step, index) => {
        if (index < currentIndex) {
            const stepEl = document.getElementById(`step-${step}`);
            if (stepEl) stepEl.classList.add('completed');
        }
    });
}

// ==================== API Calls ====================

async function loadFeaturedQuests() {
    try {
        const response = await fetch('/api/featured-quests');
        const data = await response.json();
        renderFeaturedQuests(data.quests || []);
    } catch (error) {
        console.error('Error loading featured quests:', error);
    }
}

function renderFeaturedQuests(quests) {
    const container = document.getElementById('featured-quests');
    if (!container) return;

    container.innerHTML = quests.map(quest => `
        <div class="quest-card" onclick="startFeaturedQuest('${quest.title}')">
            <div class="quest-icon">${quest.icon}</div>
            <div class="quest-title">${quest.title.toUpperCase()}</div>
            <div class="quest-description">${quest.description}</div>
            <div class="quest-xp">+${quest.xp_per_level ? quest.xp_per_level[0] : 295} XP</div>
        </div>
    `).join('');
}

function startFeaturedQuest(topic) {
    document.getElementById('topic-input').value = topic;
    startLearning();
}

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const stats = await response.json();
        updateStatsDisplay(stats);
        renderAchievements(stats.achievements || []);
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

function updateStatsDisplay(stats) {
    document.getElementById('level-badge').textContent = stats.level || 1;
    document.getElementById('xp-current').textContent = stats.xp || 0;
    document.getElementById('xp-bar-fill').style.width = `${stats.xp_progress_percent || 0}%`;
    document.getElementById('streak-count').textContent = stats.streak || 0;
    document.getElementById('achievement-count').textContent =
        `${(stats.achievements || []).length}/${stats.total_achievements || 11}`;
}

// ==================== Learning Flow ====================

async function startLearning() {
    const topic = document.getElementById('topic-input').value.trim();
    if (!topic) {
        alert('Please enter a topic!');
        return;
    }

    showLoading('Generating your adventure...');

    try {
        const userApiKey = getUserApiKey();
        const response = await fetch('/api/session/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic, api_key: userApiKey || undefined })
        });

        const data = await response.json();

        // Check for error response
        if (data.error || !response.ok) {
            hideLoading();
            alert(data.message || 'Unable to generate content. Please try a Featured Quest instead!');
            return;
        }

        currentSession = {
            id: data.session_id,
            topic: data.topic,
            aiGenerated: data.ai_generated,
            source: data.source
        };

        // Show session UI
        document.getElementById('topic-section').style.display = 'none';
        document.getElementById('session-container').style.display = 'flex';
        document.getElementById('sidebar-topic').textContent = data.topic;

        // Display story
        document.getElementById('story-title').textContent = data.story.title;
        document.getElementById('story-content').innerHTML = formatStoryContent(data.story.content);

        // Activate story step and update level display
        activateStep('story');
        updateSidebarLevels(currentLevel);

        hideLoading();

        // Log content source
        console.log(`✅ Content loaded (source: ${data.source})`);
    } catch (error) {
        hideLoading();
        alert('Error starting session. Please try a Featured Quest!');
        console.error(error);
    }
}

async function completeStory() {
    if (!currentSession) return;

    stopTTS();
    showLoading('Loading quiz...');

    try {
        const response = await fetch(`/api/session/${currentSession.id}/complete-story`, {
            method: 'POST'
        });

        const data = await response.json();

        // Show XP earned
        showXPPopup(data.xp_earned);

        // Render quiz (already generated!)
        renderQuiz(data.quiz);

        // Switch to quiz mode
        document.getElementById('story-mode').style.display = 'none';
        document.getElementById('quiz-mode').style.display = 'block';
        activateStep('quiz');

        hideLoading();
        loadStats();
    } catch (error) {
        hideLoading();
        alert('Error completing story. Please try again.');
        console.error(error);
    }
}

async function submitQuiz() {
    if (!currentSession) return;

    // Collect answers
    const questions = document.querySelectorAll('.quiz-question');
    selectedQuizAnswers = [];

    questions.forEach((q, idx) => {
        const selected = q.querySelector('.option-item.selected');
        selectedQuizAnswers.push(selected ? parseInt(selected.dataset.index) : -1);
    });

    showLoading('Checking answers...');

    try {
        const response = await fetch(`/api/session/${currentSession.id}/submit-quiz`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answers: selectedQuizAnswers })
        });

        const data = await response.json();

        // Show results
        showQuizResults(data);
        showXPPopup(data.xp_earned);

        hideLoading();
        loadStats();

        // Auto-continue to master after 2 seconds
        setTimeout(() => {
            document.getElementById('quiz-mode').style.display = 'none';
            document.getElementById('master-mode').style.display = 'block';
            document.getElementById('quiz-results').style.display = 'none';
            document.getElementById('submit-quiz-btn').style.display = 'block';
            activateStep('master');

            // Render master questions from API response (pre-generated!)
            renderMasterQuestions(data.master);
        }, 2000);

    } catch (error) {
        hideLoading();
        alert('Error submitting quiz. Please try again.');
        console.error(error);
    }
}

async function submitMaster() {
    if (!currentSession) return;

    // Collect answers from master questions
    const questions = document.querySelectorAll('.master-question');
    selectedMasterAnswers = [];

    questions.forEach((q, idx) => {
        const selected = q.querySelector('.option-item.selected');
        if (selected) {
            selectedMasterAnswers.push(selected.dataset.value);
        } else {
            selectedMasterAnswers.push('');
        }
    });

    showLoading('Evaluating your mastery...');

    try {
        const response = await fetch(`/api/session/${currentSession.id}/submit-master`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answers: selectedMasterAnswers })
        });

        const data = await response.json();

        // Show results
        showMasterResults(data);
        showXPPopup(data.xp_earned);

        hideLoading();
        loadStats();

        // Auto-continue to detective after 2 seconds
        setTimeout(() => {
            document.getElementById('master-mode').style.display = 'none';
            document.getElementById('detective-mode').style.display = 'block';
            document.getElementById('master-results').style.display = 'none';
            document.getElementById('submit-master-btn').style.display = 'block';
            activateStep('detective');

            // Render detective case from API response (pre-generated!)
            renderDetective(data.detective);
        }, 2000);

    } catch (error) {
        hideLoading();
        alert('Error submitting master practice. Please try again.');
        console.error(error);
    }
}

async function solveCase() {
    if (!currentSession) return;

    const answer = document.getElementById('detective-answer').value.trim();
    if (!answer) {
        alert('Please enter your answer!');
        return;
    }

    showLoading('Checking your solution...');

    try {
        const response = await fetch(`/api/session/${currentSession.id}/solve-case`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answer })
        });

        const data = await response.json();

        // Show results
        showDetectiveResults(data);
        showXPPopup(data.xp_earned);

        hideLoading();
        loadStats();

        // Show completion after 2 seconds
        setTimeout(() => {
            document.getElementById('detective-mode').style.display = 'none';
            document.getElementById('session-complete').style.display = 'block';
            document.getElementById('total-xp-earned').textContent = `+${data.total_session_xp || 0} XP`;
            updateLevelProgress(currentLevel);
        }, 2000);

    } catch (error) {
        hideLoading();
        alert('Error solving case. Please try again.');
        console.error(error);
    }
}

function newAdventure() {
    currentSession = null;
    currentLevel = 1;  // Reset level for new quest
    document.getElementById('session-container').style.display = 'none';
    document.getElementById('topic-section').style.display = 'block';
    document.getElementById('topic-input').value = '';

    // Reset all modes
    document.getElementById('story-mode').style.display = 'block';
    document.getElementById('quiz-mode').style.display = 'none';
    document.getElementById('master-mode').style.display = 'none';
    document.getElementById('detective-mode').style.display = 'none';
    document.getElementById('session-complete').style.display = 'none';

    // Reset result displays
    document.getElementById('quiz-results').style.display = 'none';
    document.getElementById('master-results').style.display = 'none';
    document.getElementById('detective-results').style.display = 'none';
    document.getElementById('detective-answer').value = '';

    // Reset progress steps
    document.querySelectorAll('.progress-step-v').forEach(step => {
        step.classList.remove('active', 'completed');
    });
}

// ==================== UI Rendering ====================

function formatStoryContent(content) {
    return content.split('\n').filter(p => p.trim()).map(p => `<p>${p}</p>`).join('');
}

function renderQuiz(quiz) {
    const container = document.getElementById('quiz-questions');
    container.innerHTML = '';

    quiz.questions.forEach((q, idx) => {
        const questionHtml = `
            <div class="quiz-question" data-index="${idx}">
                <div class="question-number">Question ${idx + 1}</div>
                <div class="question-text">${q.question}</div>
                <div class="options-list">
                    ${q.options.map((opt, optIdx) => `
                        <div class="option-item" data-index="${optIdx}" onclick="selectOption(this, ${idx})">
                            <span class="option-letter">${String.fromCharCode(65 + optIdx)}</span>
                            <span>${opt}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
        container.innerHTML += questionHtml;
    });
}

function renderMasterQuestions(master) {
    const container = document.getElementById('master-questions');
    container.innerHTML = '<p class="mode-info">Answer these advanced questions to prove your mastery!</p>';

    master.questions.forEach((q, idx) => {
        const questionHtml = `
            <div class="master-question" data-index="${idx}">
                <div class="question-number">Advanced Question ${idx + 1}</div>
                <div class="question-text">${q.question}</div>
                <div class="options-list">
                    ${q.options.map((opt, optIdx) => `
                        <div class="option-item" data-value="${opt}" onclick="selectMasterOption(this, ${idx})">
                            <span class="option-letter">${String.fromCharCode(65 + optIdx)}</span>
                            <span>${opt}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
        container.innerHTML += questionHtml;
    });
}

function renderDetective(detective) {
    if (!detective) return;

    document.getElementById('case-title').textContent = detective.case_title;
    document.getElementById('case-scenario').innerHTML = formatStoryContent(detective.scenario);

    const cluesHtml = detective.clues.map(c => `
        <div class="clue-item">
            <span class="clue-icon">🔎</span>
            <span>${c.description}</span>
        </div>
    `).join('');
    document.getElementById('case-clues').innerHTML = cluesHtml;

    // Format question with options
    const questionText = detective.question.replace(/\n/g, '<br>');
    document.getElementById('case-question').innerHTML = `<strong>❓ ${questionText}</strong>`;
}

function selectOption(element, questionIdx) {
    const question = element.closest('.quiz-question');
    question.querySelectorAll('.option-item').forEach(opt => opt.classList.remove('selected'));
    element.classList.add('selected');
}

function selectMasterOption(element, questionIdx) {
    const question = element.closest('.master-question');
    question.querySelectorAll('.option-item').forEach(opt => opt.classList.remove('selected'));
    element.classList.add('selected');
}

function showQuizResults(data) {
    const container = document.getElementById('quiz-results');
    const passed = data.passed ? '✅ Passed!' : '❌ Keep trying!';

    container.innerHTML = `
        <div class="result-card">
            <div class="result-icon">${data.passed ? '🎉' : '📚'}</div>
            <div class="result-title">${passed}</div>
            <div class="result-stats">${data.correct}/${data.total} correct (${data.percentage}%)</div>
            <div class="result-xp">+${data.xp_earned} XP</div>
            <p>Moving to Master Practice...</p>
        </div>
    `;
    container.style.display = 'block';
    document.getElementById('submit-quiz-btn').style.display = 'none';
}

function showMasterResults(data) {
    const container = document.getElementById('master-results');
    const mastered = data.mastered ? '🏆 Mastered!' : '📖 Good effort!';

    container.innerHTML = `
        <div class="result-card">
            <div class="result-icon">${data.mastered ? '🏆' : '💪'}</div>
            <div class="result-title">${mastered}</div>
            <div class="result-stats">${data.correct}/${data.total} correct (${data.percentage}%)</div>
            <div class="result-xp">+${data.xp_earned} XP</div>
            <p>Get ready for Detective Mode...</p>
        </div>
    `;
    container.style.display = 'block';
    document.getElementById('submit-master-btn').style.display = 'none';
}

function showDetectiveResults(data) {
    const container = document.getElementById('detective-results');
    const solved = data.solved ? '🎉 Case Solved!' : '🔍 Close, but not quite!';

    container.innerHTML = `
        <div class="result-card">
            <div class="result-icon">${data.solved ? '🕵️' : '🤔'}</div>
            <div class="result-title">${solved}</div>
            <div class="result-stats">Answer: ${data.correct_answer}</div>
            <div class="result-explanation">${data.explanation}</div>
            <div class="result-xp">+${data.xp_earned} XP</div>
        </div>
    `;
    container.style.display = 'block';
    document.getElementById('solve-case-btn').style.display = 'none';
}

function activateStep(stepName) {
    const steps = ['story', 'quiz', 'master', 'detective'];
    const currentIdx = steps.indexOf(stepName);

    steps.forEach((step, idx) => {
        const el = document.getElementById(`step-${step}`);
        if (!el) return;
        el.classList.remove('active', 'completed');
        if (idx < currentIdx) {
            el.classList.add('completed');
        } else if (idx === currentIdx) {
            el.classList.add('active');
        }
    });
}

function renderAchievements(unlockedList) {
    const container = document.getElementById('achievements-grid');
    const unlockedIds = unlockedList.map(a => a.id);

    let html = '';
    for (const [id, achievement] of Object.entries(ALL_ACHIEVEMENTS)) {
        const isUnlocked = unlockedIds.includes(id);
        html += `
            <div class="achievement-item ${isUnlocked ? '' : 'locked'}">
                <div class="achievement-icon">${achievement.icon}</div>
                <div class="achievement-name">${achievement.name}</div>
            </div>
        `;
    }

    container.innerHTML = html;
}

// ==================== TTS ====================

function toggleTTS() {
    if (isSpeaking) {
        stopTTS();
    } else {
        startTTS();
    }
}

function startTTS() {
    const content = document.getElementById('story-content').innerText;
    if (!content || !('speechSynthesis' in window)) return;

    ttsUtterance = new SpeechSynthesisUtterance(content);
    ttsUtterance.rate = 0.9;
    ttsUtterance.onend = () => {
        isSpeaking = false;
        document.getElementById('tts-btn').innerHTML = '<span>🔊</span> Listen';
    };

    speechSynthesis.speak(ttsUtterance);
    isSpeaking = true;
    document.getElementById('tts-btn').innerHTML = '<span>🔇</span> STOP';
}

function stopTTS() {
    speechSynthesis.cancel();
    isSpeaking = false;
    document.getElementById('tts-btn').innerHTML = '<span>🔊</span> LISTEN';
}

// ==================== Utilities ====================

function showLoading(text = 'Loading...') {
    document.getElementById('loading-text').textContent = text;
    document.getElementById('loading-overlay').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loading-overlay').style.display = 'none';
}

function showXPPopup(amount) {
    const popup = document.getElementById('xp-popup');
    const value = document.getElementById('xp-popup-value');

    value.textContent = `+${amount} XP`;
    popup.style.display = 'block';

    setTimeout(() => {
        popup.style.display = 'none';
    }, 2000);
}

// ==================== Achievements Modal ====================

function showAchievements() {
    const modal = document.getElementById('achievements-modal');
    if (modal) {
        modal.style.display = 'flex';
    }
}

function closeAchievements(event) {
    // If called from overlay click, check if click was on overlay itself
    if (event && event.target !== event.currentTarget) return;
    const modal = document.getElementById('achievements-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// ==================== Level Progression ====================

function updateSidebarLevels(currentLvl) {
    // Update sidebar level indicators
    for (let i = 1; i <= 3; i++) {
        const el = document.getElementById(`sidebar-lvl-${i}`);
        if (el) {
            el.classList.remove('active', 'completed', 'locked');
            if (i < currentLvl) {
                el.classList.add('completed');
                el.textContent = `✓ ${i}`;
            } else if (i === currentLvl) {
                el.classList.add('active');
                el.textContent = `LVL ${i}`;
            } else {
                el.classList.add('locked');
                el.textContent = `🔒 ${i}`;
            }
        }
    }
}

function updateLevelProgress(completedLevel) {
    // Update completion screen level dots
    for (let i = 1; i <= 3; i++) {
        const dot = document.getElementById(`lvl-${i}`);
        if (dot) {
            dot.classList.remove('completed', 'unlocked');
            if (i <= completedLevel) {
                dot.classList.add('completed');
            } else if (i === completedLevel + 1) {
                dot.classList.add('unlocked');
            }
        }
    }

    // Update completion text
    document.getElementById('completed-level').textContent = completedLevel;

    // Show/hide next level button
    const nextBtn = document.getElementById('next-level-btn');
    const nextNum = document.getElementById('next-level-num');

    if (completedLevel < maxLevel) {
        nextBtn.style.display = 'inline-flex';
        nextNum.textContent = completedLevel + 1;
        document.getElementById('completion-message').textContent = `Level ${completedLevel + 1} is now unlocked!`;
    } else {
        nextBtn.style.display = 'none';
        document.getElementById('completion-message').textContent = "🎉 You've mastered all levels!";
    }
}

async function startNextLevel() {
    if (!currentSession || currentLevel >= maxLevel) return;

    currentLevel++;
    // Strip any existing level info from topic before adding new level
    let baseTopic = currentSession.topic.split('(')[0].trim();

    showLoading(`Loading Level ${currentLevel}...`);

    try {
        // Start new session at next level
        const response = await fetch('/api/session/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: `${baseTopic} (Level ${currentLevel} - Advanced)` })
        });

        const data = await response.json();

        if (data.error || !response.ok) {
            hideLoading();
            alert(data.message || 'Unable to load next level. Try again!');
            return;
        }

        currentSession = {
            id: data.session_id,
            topic: baseTopic,
            aiGenerated: data.ai_generated,
            source: data.source
        };

        // Reset UI for new level
        selectedQuizAnswers = [];
        selectedMasterAnswers = [];

        // Hide the level complete modal first
        const modal = document.getElementById('level-complete-modal');
        if (modal) modal.style.display = 'none';

        // Show story for new level
        document.getElementById('story-title').textContent = data.story.title;
        document.getElementById('story-content').innerHTML = formatStoryContent(data.story.content);

        // Reset all sections - hide all mode sections
        document.querySelectorAll('.mode-section').forEach(section => {
            section.style.display = 'none';
        });

        // Show story section (the container, not story-mode)
        const storySection = document.getElementById('story-section') || document.getElementById('story-mode');
        if (storySection) storySection.style.display = 'block';

        // Reset all result displays (hide old results from previous level)
        document.getElementById('quiz-results').style.display = 'none';
        document.getElementById('master-results').style.display = 'none';
        document.getElementById('detective-results').style.display = 'none';

        // Restore all submit buttons
        document.getElementById('submit-quiz-btn').style.display = 'block';
        document.getElementById('submit-master-btn').style.display = 'block';
        document.getElementById('solve-case-btn').style.display = 'block';

        // Clear detective answer input
        document.getElementById('detective-answer').value = '';

        // Reset progress steps
        document.querySelectorAll('.progress-step-v').forEach(step => {
            step.classList.remove('completed', 'active');
        });

        activateStep('story');
        updateSidebarLevels(currentLevel);
        hideLoading();

        console.log(`✅ Started Level ${currentLevel}`);

    } catch (error) {
        hideLoading();
        console.error('Level loading error:', error);
        alert('Error loading next level: ' + error.message);
    }
}
