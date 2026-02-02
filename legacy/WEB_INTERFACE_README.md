# 🚀 Tokamak AI 웹 인터페이스

## ✨ 주요 기능

### 1. **현대적인 웹 채팅 인터페이스**
- 🎨 아름다운 다크 모드 UI
- 💬 실시간 스트리밍 응답
- 📝 마크다운 및 코드 하이라이팅 지원
- 💾 대화 히스토리 자동 저장

### 2. **편리한 기능들**
- 🔄 여러 AI 모델 선택 가능 (Qwen3-235B, Qwen3-80B-Next)
- 📥 대화 내용 JSON 파일로 다운로드
- 🗑️ 대화 내용 초기화
- ⚡ 빠른 프롬프트 버튼

### 3. **개발자 친화적**
- 🔧 Flask 기반 백엔드
- 📡 Server-Sent Events (SSE)를 통한 스트리밍
- 🎯 RESTful API 구조

---

## 🛠️ 설치 및 실행

### 1. 필수 패키지 설치

```bash
# 가상환경 활성화 (이미 생성되어 있음)
source .venv/bin/activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일이 이미 설정되어 있어야 합니다:

```env
AI_API_KEY=your_api_key_here
AI_BASE_URL=
AI_MODEL=qwen3-235b
```

### 3. 웹 서버 실행

```bash
# 가상환경 활성화 후
source .venv/bin/activate

# Flask 앱 실행
python app.py
```

서버가 시작되면 다음과 같은 메시지가 표시됩니다:

```
🚀 Starting Tokamak AI Chat Interface...
📡 Server running at: http://localhost:5000
🔑 Using API Key: your_api_k...
 * Running on http://127.0.0.1:5000
```

### 4. 브라우저에서 접속

브라우저를 열고 다음 주소로 접속:

```
http://localhost:5000
```

---

## 📖 사용 방법

### 기본 채팅

1. **메시지 입력**: 하단 입력창에 질문이나 요청사항 입력
2. **전송**: Enter 키를 누르거나 전송 버튼 클릭
3. **줄바꿈**: Shift + Enter로 여러 줄 입력 가능

### 빠른 프롬프트

환영 화면에서 제공되는 버튼을 클릭하여 빠르게 대화 시작:
- 👋 인사하기
- 💻 코드 예제
- 🔗 블록체인 설명
- ✨ 창작하기

### 모델 선택

상단 우측의 드롭다운 메뉴에서 사용할 AI 모델 선택:
- **Qwen3-235B**: 더 강력한 모델 (기본값)
- **Qwen3-80B-Next**: 빠른 응답

### 대화 관리

- **🗑️ 대화 지우기**: 모든 대화 내용 초기화
- **📥 대화 저장**: 대화 내용을 JSON 파일로 다운로드

---

## 🎯 프로젝트 구조

```
aiAPIcall/
├── app.py                  # Flask 백엔드 서버
├── templates/
│   └── index.html         # 메인 HTML 템플릿
├── static/
│   ├── css/
│   │   └── style.css      # 스타일시트
│   └── js/
│       └── app.js         # 프론트엔드 JavaScript
├── .env                   # 환경 변수 (API 키)
├── requirements.txt       # Python 패키지
└── simple_call.py        # 기존 CLI 버전
```

---

## 🔧 API 엔드포인트

### `GET /`
메인 웹 인터페이스 페이지

### `GET /api/models`
사용 가능한 AI 모델 목록 조회

**응답 예시:**
```json
{
  "models": ["qwen3-235b", "qwen3-80b-next"]
}
```

### `POST /api/chat`
AI와 채팅 (스트리밍 응답)

**요청 본문:**
```json
{
  "messages": [
    {"role": "user", "content": "안녕하세요"}
  ],
  "model": "qwen3-235b"
}
```

**응답:** Server-Sent Events (SSE) 스트림

### `GET /api/health`
서버 상태 확인

**응답 예시:**
```json
{
  "status": "ok",
  "timestamp": "2026-01-13T22:45:00.000000"
}
```

---

## 💡 추가 개발 아이디어

### 1. **CLI 버전과 함께 사용**

기존 CLI 버전도 계속 사용 가능:

```bash
# 간단한 호출
python simple_call.py

# 고급 기능 (스트리밍, 대화 히스토리)
python advanced_call.py
```

### 2. **확장 가능한 기능들**

- 📊 대화 통계 및 분석
- 🎨 테마 커스터마이징
- 🔐 사용자 인증
- 💬 여러 대화 세션 관리
- 🌐 다국어 지원
- 📱 모바일 최적화
- 🔍 대화 내용 검색
- 🎤 음성 입력/출력

### 3. **다른 프로젝트와 통합**

이 웹 인터페이스를 다른 프로젝트에 통합하여 사용:

```python
# 다른 Python 프로젝트에서 사용
from app import AIService

ai = AIService()
response = ai.chat_stream(
    messages=[{"role": "user", "content": "Hello"}],
    model="qwen3-235b"
)
```

---

## 🐛 문제 해결

### 포트가 이미 사용 중인 경우

`app.py`의 마지막 줄을 수정:

```python
app.run(debug=True, port=5001, threaded=True)  # 5001로 변경
```

### API 키 오류

`.env` 파일의 `AI_API_KEY`가 올바른지 확인

### 모듈을 찾을 수 없는 경우

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🎨 UI 스크린샷

웹 인터페이스는 다음과 같은 특징을 가지고 있습니다:

- **다크 모드**: 눈의 피로를 줄이는 세련된 다크 테마
- **그라데이션**: 현대적인 보라색-파란색 그라데이션
- **애니메이션**: 부드러운 전환 효과와 마이크로 인터랙션
- **반응형**: 모바일, 태블릿, 데스크톱 모두 지원
- **코드 하이라이팅**: 프로그래밍 언어별 구문 강조
- **마크다운 렌더링**: 서식이 적용된 텍스트 표시

---

## 📝 라이선스

이 프로젝트는 Tokamak Network AI API를 활용한 예제입니다.

---

## 🙏 기여

개선 사항이나 버그 리포트는 언제든 환영합니다!

---

**즐거운 AI 채팅 되세요! 🚀**
