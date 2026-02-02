# 🎉 Tokamak AI - 빠른 시작 가이드

## 📌 요약

Tokamak Network AI API를 **3가지 방법**으로 사용할 수 있습니다:

1. **🌐 웹 인터페이스** - 브라우저에서 사용 (가장 추천!)
2. **💻 CLI 도구** - 터미널에서 빠르게 사용
3. **📚 Python 라이브러리** - 다른 프로젝트에 통합

---

## 🚀 1분 안에 시작하기

### 웹 인터페이스 실행

```bash
# 1. 가상환경 활성화
source .venv/bin/activate

# 2. 웹 서버 시작
python app.py

# 3. 브라우저에서 열기
# http://localhost:5000
```

### CLI 도구 사용

```bash
# 단일 질문
python ai.py "Python으로 웹 크롤러 만드는 방법"

# 대화형 모드
python ai.py --chat
```

---

## 🌟 주요 기능

### 웹 인터페이스

✅ **실시간 스트리밍** - AI 답변이 실시간으로 나타남  
✅ **대화 히스토리** - 브라우저를 닫아도 대화 유지  
✅ **모델 선택** - Qwen3-235B, Qwen3-80B-Next  
✅ **마크다운 지원** - 코드 하이라이팅, 표, 리스트  
✅ **대화 저장** - JSON 파일로 다운로드  
✅ **빠른 프롬프트** - 자주 사용하는 질문 버튼  

### CLI 도구

✅ **빠른 질문** - 터미널에서 즉시 답변  
✅ **대화형 모드** - 연속 대화 가능  
✅ **스크립트 통합** - 자동화에 활용  
✅ **모델 선택** - 명령줄 옵션으로 선택  

---

## 📖 사용 예제

### 웹 인터페이스

1. **브라우저에서 http://localhost:5000 열기**
2. **빠른 프롬프트 버튼 클릭** 또는 **직접 질문 입력**
3. **AI의 실시간 답변 확인**
4. **대화 계속하기** - 이전 대화를 기억합니다!

### CLI 도구

```bash
# 코딩 질문
python ai.py "FastAPI로 REST API 만드는 방법"

# 창작 요청
python ai.py "오늘 기분 좋아지는 시 하나 써줘"

# 대화형 모드
python ai.py --chat
You: 블록체인이란?
AI: [상세한 설명]
You: 스마트 컨트랙트는?
AI: [이전 대화를 기억하며 답변]
```

### Python 코드

```python
from ai import TokamakAI

ai = TokamakAI()

# 질문하기
response = ai.ask("Python 비동기 프로그래밍 설명해줘", stream=False)
print(response)

# 대화형 모드
ai.chat()
```

---

## 🎯 언제 무엇을 사용할까?

| 상황 | 추천 방법 | 이유 |
|------|----------|------|
| 일상적인 AI 채팅 | 🌐 웹 인터페이스 | 편리한 UI, 대화 히스토리 |
| 빠른 질문 | 💻 CLI 도구 | 터미널에서 즉시 사용 |
| 자동화/스크립트 | 💻 CLI 도구 | 쉬운 통합 |
| 다른 프로젝트에 통합 | 📚 Python 라이브러리 | 유연한 커스터마이징 |
| 코드 작성 도움 | 🌐 웹 인터페이스 | 코드 하이라이팅 |
| 배치 처리 | 📚 Python 라이브러리 | 프로그래밍 제어 |

---

## 📁 파일 설명

### 핵심 파일

- **`app.py`** - 웹 서버 (Flask)
- **`ai.py`** - CLI 도구 & Python 라이브러리
- **`templates/index.html`** - 웹 UI
- **`static/css/style.css`** - 스타일
- **`static/js/app.js`** - 프론트엔드 로직

### 문서

- **`README.md`** - 완벽 가이드 (이 파일)
- **`WEB_INTERFACE_README.md`** - 웹 인터페이스 상세 가이드
- **`QUICKSTART.md`** - 빠른 시작 가이드

### 기존 파일

- **`simple_call.py`** - 기본 API 호출 예제
- **`advanced_call.py`** - 고급 기능 예제
- **`list_models.py`** - 모델 목록 조회

---

## 💡 유용한 팁

### 웹 인터페이스

- **Enter** - 메시지 전송
- **Shift + Enter** - 줄바꿈
- **상단 우측 드롭다운** - 모델 변경
- **🗑️ 버튼** - 대화 내용 지우기
- **📥 버튼** - 대화 내용 저장

### CLI 도구

```bash
# 도움말 보기
python ai.py --help

# 사용 가능한 모델 확인
python ai.py --list-models

# 다른 모델 사용
python ai.py --model qwen3-80b-next "질문"

# 스트리밍 없이 전체 응답
python ai.py --no-stream "질문"
```

---

## 🔧 문제 해결

### 웹 서버가 시작되지 않을 때

```bash
# 가상환경 확인
source .venv/bin/activate

# Flask 설치 확인
pip install flask

# 다른 포트 사용 (app.py 수정)
# app.run(debug=True, port=5001)
```

### API 키 오류

```bash
# .env 파일 확인
cat .env

# API 키가 올바른지 확인
AI_API_KEY=your_api_key_here
```

### 모듈을 찾을 수 없을 때

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 다음 단계

### 더 알아보기

1. **완벽 가이드** - `README.md` 읽기
2. **웹 인터페이스 상세** - `WEB_INTERFACE_README.md` 읽기
3. **예제 코드** - `simple_call.py`, `advanced_call.py` 확인

### 확장하기

- 음성 입력/출력 추가
- 파일 업로드 기능
- 커스텀 플러그인
- 모바일 앱
- VS Code 확장

---

## 📞 도움이 필요하신가요?

- **문서 확인**: `README.md`, `WEB_INTERFACE_README.md`
- **예제 코드**: `simple_call.py`, `advanced_call.py`
- **API 문서**: Tokamak Network 공식 문서

---

**즐거운 AI 활용 되세요! 🎉✨**

---

## 📸 스크린샷

### 웹 인터페이스

![웹 인터페이스](/.gemini/antigravity/brain/818ee65b-129a-4451-853d-6de8306c6921/ai_chat_interface_1768312832989.png)

### 채팅 예제

![채팅 예제](/.gemini/antigravity/brain/818ee65b-129a-4451-853d-6de8306c6921/chat_functionality_test_1768313024733.png)

---

## 🎨 특징

- **🌙 다크 모드** - 눈의 피로 감소
- **🎨 그라데이션** - 현대적인 디자인
- **✨ 애니메이션** - 부드러운 전환
- **📱 반응형** - 모든 기기 지원
- **💻 코드 하이라이팅** - 프로그래밍 언어별 구문 강조
- **📝 마크다운** - 서식 있는 텍스트

---

**Made with ❤️ for Tokamak Network**
