# 🚀 Tokamak AI - 완벽 가이드

Tokamak Network AI API를 더 쉽고 유용하게 사용하기 위한 완전한 솔루션입니다!

---

## 📦 프로젝트 구성

이 프로젝트는 **4가지 방법**으로 AI를 사용할 수 있습니다:

### 1. 🌐 **웹 인터페이스** (일반 채팅용)
- 브라우저에서 사용하는 현대적인 채팅 UI
- 실시간 스트리밍 응답
- 대화 히스토리 자동 저장
- 마크다운 & 코드 하이라이팅

### 2. 💻 **CLI 도구** (빠른 질문용)
- 터미널에서 빠르게 질문
- 대화형 모드 지원
- 스크립트에서 사용 가능

### 3. 🛠️ **Code Assistant** (코드 개발용) ⭐ NEW!
- 파일/프로젝트 자동 분석
- 코드 리뷰, 리팩토링, 버그 찾기
- 테스트 코드 자동 생성
- 개발 워크플로우에 최적화

### 4. 📚 **Python 라이브러리** (프로젝트 통합용)
- 다른 프로젝트에 통합
- 커스터마이징 가능

---

## 🚀 빠른 시작

### 1️⃣ 웹 인터페이스 실행

```bash
# 가상환경 활성화
source .venv/bin/activate

# 웹 서버 시작
python app.py
```

브라우저에서 열기: **http://localhost:5000**

### 2️⃣ CLI 도구 사용

```bash
# 단일 질문
python ai.py "Python으로 웹 크롤러 만드는 방법"

# 대화형 모드
python ai.py --chat

# 다른 모델 사용
python ai.py --model qwen3-80b-next "블록체인이란?"
```

### 3️⃣ Code Assistant 사용 (코드 개발용) ⭐

```bash
# 프로젝트 전체 분석
python code_assistant.py analyze-dir .

# 파일 분석
python code_assistant.py analyze app.py

# 코드 리뷰
python code_assistant.py review app.py

# 버그 찾기
python code_assistant.py bugs app.py

# 리팩토링
python code_assistant.py refactor app.py

# 자세한 사용법
python code_assistant.py --help
```

### 4️⃣ Python 코드에서 사용

```python
from ai import TokamakAI

# AI 인스턴스 생성
ai = TokamakAI()

# 질문하기
response = ai.ask("안녕하세요!")
print(response)

# 대화형 모드
ai.chat()
```

---

## 🎨 웹 인터페이스 기능

### ✨ 주요 기능

1. **실시간 스트리밍**
   - AI의 답변이 실시간으로 나타남
   - 긴 답변도 기다릴 필요 없음

2. **대화 히스토리**
   - 브라우저를 닫아도 대화 내용 유지
   - LocalStorage에 자동 저장

3. **모델 선택**
   - Qwen3-235B (더 강력)
   - Qwen3-80B-Next (더 빠름)

4. **빠른 프롬프트**
   - 자주 사용하는 질문을 버튼으로
   - 클릭 한 번으로 대화 시작

5. **대화 관리**
   - 대화 내용 JSON으로 저장
   - 대화 내용 초기화

6. **마크다운 지원**
   - 서식이 적용된 텍스트
   - 코드 블록 하이라이팅
   - 표, 리스트 등 지원

### 🎯 사용 팁

- **Enter**: 메시지 전송
- **Shift + Enter**: 줄바꿈
- **빠른 프롬프트**: 환영 화면의 버튼 클릭
- **모델 변경**: 상단 우측 드롭다운

---

## 💻 CLI 도구 사용법

### 기본 사용

```bash
# 단일 질문 (스트리밍)
python ai.py "질문 내용"

# 스트리밍 없이 전체 응답
python ai.py --no-stream "질문 내용"
```

### 대화형 모드

```bash
python ai.py --chat
```

대화형 모드에서는:
- 연속적인 대화 가능
- 이전 대화 내용을 기억
- `exit`, `quit`, `q`로 종료

### 모델 선택

```bash
# Qwen3-235B (기본값)
python ai.py "질문"

# Qwen3-80B-Next
python ai.py --model qwen3-80b-next "질문"
```

### 사용 가능한 모델 확인

```bash
python ai.py --list-models
```

### 도움말

```bash
python ai.py --help
```

---

## 📚 Python 라이브러리로 사용

### 기본 사용

```python
from ai import TokamakAI

# AI 인스턴스 생성
ai = TokamakAI()

# 질문하기 (스트리밍)
ai.ask("Python으로 웹 크롤러 만드는 방법")

# 스트리밍 없이
response = ai.ask("블록체인이란?", stream=False)
print(response)
```

### 모델 선택

```python
# Qwen3-80B-Next 사용
ai = TokamakAI(model="qwen3-80b-next")
response = ai.ask("안녕하세요")
```

### 대화형 사용

```python
ai = TokamakAI()
ai.chat()  # 터미널에서 대화형 모드 시작
```

### 다른 프로젝트에 통합

```python
from ai import TokamakAI

class MyApp:
    def __init__(self):
        self.ai = TokamakAI()
    
    def get_ai_response(self, user_input):
        return self.ai.ask(user_input, stream=False)
    
    def process_data(self, data):
        prompt = f"다음 데이터를 분석해줘: {data}"
        analysis = self.ai.ask(prompt, stream=False)
        return analysis
```

---

## 🛠️ 고급 사용법

### 웹 API 직접 호출

웹 인터페이스는 RESTful API를 제공합니다:

```python
import requests
import json

# 채팅 API 호출
url = "http://localhost:5000/api/chat"
data = {
    "messages": [
        {"role": "user", "content": "안녕하세요"}
    ],
    "model": "qwen3-235b"
}

response = requests.post(url, json=data, stream=True)

# 스트리밍 응답 처리
for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data: '):
            data = line[6:]
            if data != '[DONE]':
                chunk = json.loads(data)
                print(chunk['content'], end='', flush=True)
```

### 커스텀 시스템 프롬프트

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url=os.getenv("AI_BASE_URL")
)

response = client.chat.completions.create(
    model="qwen3-235b",
    messages=[
        {
            "role": "system", 
            "content": "당신은 블록체인 전문가입니다. 기술적인 질문에 상세히 답변해주세요."
        },
        {
            "role": "user", 
            "content": "스마트 컨트랙트란?"
        }
    ]
)

print(response.choices[0].message.content)
```

### 배치 처리

```python
from ai import TokamakAI

ai = TokamakAI()

questions = [
    "Python이란?",
    "JavaScript란?",
    "Rust란?"
]

answers = []
for q in questions:
    print(f"\n질문: {q}")
    answer = ai.ask(q, stream=False)
    answers.append({"question": q, "answer": answer})
    print(f"답변: {answer[:100]}...")

# 결과 저장
import json
with open('batch_results.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
```

---

## 📁 프로젝트 구조

```
aiAPIcall/
├── app.py                    # Flask 웹 서버
├── ai.py                     # CLI 도구 & Python 라이브러리
├── simple_call.py           # 기본 예제
├── advanced_call.py         # 고급 예제
├── .env                     # 환경 변수 (API 키)
├── requirements.txt         # Python 패키지
├── templates/
│   └── index.html          # 웹 UI 템플릿
├── static/
│   ├── css/
│   │   └── style.css       # 스타일시트
│   └── js/
│       └── app.js          # 프론트엔드 JavaScript
└── WEB_INTERFACE_README.md # 웹 인터페이스 상세 가이드
```

---

## 🎯 사용 시나리오

### 1. 코드 개발 도우미

```bash
# CLI로 빠르게 질문
python ai.py "Python에서 비동기 프로그래밍하는 방법"

# 웹에서 대화하며 코드 작성
# http://localhost:5000 접속 후 대화
```

### 2. 문서 작성

```python
from ai import TokamakAI

ai = TokamakAI()

# 기술 문서 작성
prompt = """
다음 주제로 기술 문서를 작성해줘:
- 주제: REST API 설계 베스트 프랙티스
- 형식: 마크다운
- 길이: 1000자 정도
"""

doc = ai.ask(prompt, stream=False)
with open('api_guide.md', 'w', encoding='utf-8') as f:
    f.write(doc)
```

### 3. 데이터 분석

```python
from ai import TokamakAI
import pandas as pd

ai = TokamakAI()

# 데이터 읽기
df = pd.read_csv('sales_data.csv')

# AI에게 분석 요청
prompt = f"""
다음 판매 데이터를 분석해줘:
{df.describe().to_string()}

다음을 포함해서 분석해줘:
1. 주요 트렌드
2. 이상치
3. 개선 제안
"""

analysis = ai.ask(prompt, stream=False)
print(analysis)
```

### 4. 자동화 스크립트

```bash
#!/bin/bash
# daily_summary.sh

# 오늘의 뉴스 요약
python ai.py "오늘의 블록체인 뉴스를 3줄로 요약해줘" --no-stream > daily_news.txt

# 이메일로 전송
mail -s "Daily AI Summary" user@example.com < daily_news.txt
```

---

## 🔧 환경 설정

### .env 파일

```env
AI_API_KEY=your_api_key_here
AI_BASE_URL=https://
AI_MODEL=
```

### 필수 패키지

```txt
openai
python-dotenv
flask
```

설치:
```bash
pip install -r requirements.txt
```

---

## 💡 팁 & 트릭

### 1. 효과적인 프롬프트 작성

**좋은 예:**
```
"Python으로 웹 크롤러를 만들고 싶어. 
BeautifulSoup을 사용해서 네이버 뉴스 제목을 
가져오는 코드를 작성해줘. 주석도 포함해줘."
```

**나쁜 예:**
```
"웹 크롤러 만들어줘"
```

### 2. 대화 맥락 활용

웹 인터페이스나 대화형 모드에서는 이전 대화를 기억하므로:

```
You: Python으로 API 서버 만드는 방법 알려줘
AI: [Flask 예제 코드 제공]

You: 이제 여기에 인증 기능을 추가해줘
AI: [인증 기능이 추가된 코드 제공]
```

### 3. 모델 선택 가이드

- **Qwen3-235B**: 복잡한 질문, 긴 답변 필요시
- **Qwen3-80B-Next**: 빠른 응답 필요시, 간단한 질문

### 4. 배치 처리 최적화

```python
from ai import TokamakAI
import time

ai = TokamakAI()

# 여러 질문을 효율적으로 처리
questions = [...]

for i, q in enumerate(questions):
    print(f"Processing {i+1}/{len(questions)}")
    answer = ai.ask(q, stream=False)
    # 저장 로직
    time.sleep(1)  # API 레이트 리밋 고려
```

---

## 🐛 문제 해결

### 포트 충돌

```python
# app.py 수정
app.run(debug=True, port=5001, threaded=True)
```

### API 키 오류

```bash
# .env 파일 확인
cat .env

# 환경 변수 확인
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('AI_API_KEY'))"
```

### 모듈 없음 오류

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 다음 단계

### 추가 기능 아이디어

1. **음성 입력/출력**
   - 음성으로 질문하고 답변 듣기
   - Web Speech API 활용

2. **파일 업로드**
   - 문서 분석
   - 이미지 설명

3. **플러그인 시스템**
   - 커스텀 기능 추가
   - 외부 API 통합

4. **모바일 앱**
   - React Native
   - Flutter

5. **VS Code 확장**
   - 코드 에디터에서 바로 사용
   - 코드 리뷰, 설명 생성

---

## 📝 라이선스

이 프로젝트는 Tokamak Network AI API를 활용한 예제입니다.

---

## 🙏 기여

개선 사항이나 버그 리포트는 언제든 환영합니다!

---

**Happy Coding with Tokamak AI! 🚀✨**
