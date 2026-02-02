// App State
let conversationHistory = [];
let isProcessing = false;

// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const downloadBtn = document.getElementById('downloadBtn');
const modelSelect = document.getElementById('modelSelect');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    loadConversationHistory();
    loadModels(); // 모델 목록 로드 추가
    autoResizeTextarea();
});

// Load models from server
async function loadModels() {
    try {
        const response = await fetch('/api/models');
        const data = await response.json();

        if (data.models && data.models.length > 0) {
            modelSelect.innerHTML = data.models.map(model =>
                `<option value="${model}">${model}</option>`
            ).join('');

            // 이전에 선택했던 모델이 있으면 복구 (구현 전이면 기본값)
            const savedModel = localStorage.getItem('selectedModel');
            if (savedModel && data.models.includes(savedModel)) {
                modelSelect.value = savedModel;
            }
        }
    } catch (error) {
        console.error('Failed to load models:', error);
    }
}

// Event Listeners
function setupEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    clearBtn.addEventListener('click', clearConversation);
    downloadBtn.addEventListener('click', downloadConversation);

    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    userInput.addEventListener('input', autoResizeTextarea);

    // Model selection change
    modelSelect.addEventListener('change', () => {
        localStorage.setItem('selectedModel', modelSelect.value);
    });

    // Quick prompts
    document.querySelectorAll('.quick-prompt').forEach(btn => {
        btn.addEventListener('click', () => {
            userInput.value = btn.dataset.prompt;
            sendMessage();
        });
    });
}

// Auto-resize textarea
function autoResizeTextarea() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 200) + 'px';
}

// Send Message
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message || isProcessing) return;

    isProcessing = true;
    sendBtn.disabled = true;

    // Hide welcome message
    const welcomeMsg = document.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.style.display = 'none';
    }

    // Add user message
    addMessage('user', message);
    conversationHistory.push({ role: 'user', content: message });

    // Clear input
    userInput.value = '';
    autoResizeTextarea();

    // Add assistant message placeholder
    const assistantMsgId = addMessage('assistant', '', true);

    try {
        await streamResponse(assistantMsgId);
    } catch (error) {
        console.error('Error:', error);
        updateMessage(assistantMsgId, `❌ 오류가 발생했습니다: ${error.message}`);
    } finally {
        isProcessing = false;
        sendBtn.disabled = false;
        userInput.focus();
        saveConversationHistory();
    }
}

// Stream Response
async function streamResponse(messageId) {
    const model = modelSelect.value;
    const messageElement = document.getElementById(messageId);
    const contentElement = messageElement.querySelector('.message-content');

    let fullResponse = '';

    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            messages: conversationHistory,
            model: model
        })
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
            if (line.startsWith('data: ')) {
                const data = line.slice(6);
                if (data === '[DONE]') {
                    conversationHistory.push({ role: 'assistant', content: fullResponse });
                    return;
                }

                try {
                    const parsed = JSON.parse(data);
                    if (parsed.content) {
                        fullResponse += parsed.content;
                        contentElement.innerHTML = renderMarkdown(fullResponse);
                        highlightCode();
                        scrollToBottom();
                    }
                } catch (e) {
                    // Ignore parsing errors
                }
            }
        }
    }
}

// Add Message
function addMessage(role, content, isTyping = false) {
    const messageId = `msg-${Date.now()}-${Math.random()}`;
    const avatar = role === 'user' ? '👤' : '🤖';

    const messageHTML = `
        <div class="message ${role}" id="${messageId}">
            <div class="message-avatar">${avatar}</div>
            <div class="message-content">
                ${isTyping ? '<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>' : renderMarkdown(content)}
            </div>
        </div>
    `;

    chatContainer.insertAdjacentHTML('beforeend', messageHTML);
    scrollToBottom();

    if (!isTyping) {
        highlightCode();
    }

    return messageId;
}

// Update Message
function updateMessage(messageId, content) {
    const messageElement = document.getElementById(messageId);
    if (messageElement) {
        const contentElement = messageElement.querySelector('.message-content');
        contentElement.innerHTML = renderMarkdown(content);
        highlightCode();
    }
}

// Render Markdown
function renderMarkdown(text) {
    if (!text) return '';

    // Configure marked
    marked.setOptions({
        breaks: true,
        gfm: true,
        highlight: function (code, lang) {
            if (lang && hljs.getLanguage(lang)) {
                try {
                    return hljs.highlight(code, { language: lang }).value;
                } catch (err) { }
            }
            return hljs.highlightAuto(code).value;
        }
    });

    return marked.parse(text);
}

// Highlight Code
function highlightCode() {
    document.querySelectorAll('pre code').forEach((block) => {
        if (!block.classList.contains('hljs')) {
            hljs.highlightElement(block);
        }
    });
}

// Scroll to Bottom
function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Clear Conversation
function clearConversation() {
    if (confirm('대화 내용을 모두 지우시겠습니까?')) {
        conversationHistory = [];
        chatContainer.innerHTML = `
            <div class="welcome-message">
                <div class="welcome-icon">👋</div>
                <h2>Tokamak AI에 오신 것을 환영합니다!</h2>
                <p>무엇이든 물어보세요. AI가 도와드리겠습니다.</p>
                <div class="quick-prompts">
                    <button class="quick-prompt" data-prompt="안녕하세요! 자기소개 해주세요.">👋 인사하기</button>
                    <button class="quick-prompt" data-prompt="Python으로 간단한 웹 크롤러를 만드는 방법을 알려주세요.">💻 코드 예제</button>
                    <button class="quick-prompt" data-prompt="블록체인 기술에 대해 쉽게 설명해주세요.">🔗 블록체인 설명</button>
                    <button class="quick-prompt" data-prompt="오늘 기분 좋아지는 시를 하나 써주세요.">✨ 창작하기</button>
                </div>
            </div>
        `;

        // 새로 생성된 빠른 프롬프트 버튼에만 이벤트 리스너 추가
        document.querySelectorAll('.quick-prompt').forEach(btn => {
            btn.addEventListener('click', () => {
                userInput.value = btn.dataset.prompt;
                sendMessage();
            });
        });

        saveConversationHistory();
    }
}

// Download Conversation
function downloadConversation() {
    if (conversationHistory.length === 0) {
        alert('저장할 대화 내용이 없습니다.');
        return;
    }

    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const filename = `tokamak-ai-chat-${timestamp}.json`;

    const data = {
        timestamp: new Date().toISOString(),
        model: modelSelect.value,
        messages: conversationHistory
    };

    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}

// Save Conversation History
function saveConversationHistory() {
    try {
        localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
    } catch (e) {
        console.error('Failed to save conversation history:', e);
    }
}

// Load Conversation History
function loadConversationHistory() {
    try {
        const saved = localStorage.getItem('conversationHistory');
        if (saved) {
            conversationHistory = JSON.parse(saved);

            // Restore messages
            if (conversationHistory.length > 0) {
                const welcomeMsg = document.querySelector('.welcome-message');
                if (welcomeMsg) {
                    welcomeMsg.style.display = 'none';
                }

                conversationHistory.forEach(msg => {
                    addMessage(msg.role, msg.content);
                });
            }
        }
    } catch (e) {
        console.error('Failed to load conversation history:', e);
        conversationHistory = [];
    }
}

// Health Check
async function checkHealth() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        console.log('Server health:', data);
    } catch (error) {
        console.error('Health check failed:', error);
    }
}

// Run health check on load
checkHealth();
