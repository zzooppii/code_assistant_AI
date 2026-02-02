# 🛠️ Tokamak AI Code Assistant

## 코드 개발을 위한 AI 어시스턴트

웹 인터페이스는 일반 채팅용이고, **코드 개발**을 위해서는 이 도구를 사용하세요!

---

## 🎯 주요 기능

### 1. **파일 분석** (`analyze`)
- 코드의 주요 기능과 목적 파악
- 코드 품질 평가
- 잠재적 버그 발견
- 개선점 제안

### 2. **프로젝트 분석** (`analyze-dir`)
- 프로젝트 전체 구조 분석
- 아키텍처 평가
- 기술 스택 파악
- 전반적인 개선 제안

### 3. **코드 리뷰** (`review`)
- 전문가 관점의 코드 리뷰
- 스타일, 버그, 성능, 보안 체크
- 구체적인 개선 제안

### 4. **리팩토링** (`refactor`)
- 가독성 향상
- 중복 코드 제거
- 함수/클래스 분리
- 리팩토링된 코드 제공

### 5. **코드 설명** (`explain`)
- 초보자도 이해할 수 있는 설명
- 각 부분의 역할 설명
- 사용된 개념/패턴 설명

### 6. **버그 찾기** (`bugs`)
- 논리적 오류 발견
- 예외 처리 누락 체크
- 보안 취약점 발견
- 수정 방법 제시

### 7. **테스트 생성** (`test`)
- 단위 테스트 자동 생성
- 엣지 케이스 테스트
- 실행 가능한 테스트 코드

### 8. **코드 직접 수정** (`apply`)
- AI 지시사항에 따라 파일을 읽고 즉시 수정
- 수정 전 백업 파일(.bak) 자동 생성
- 전체 코드를 다시 작성하여 적용

---

## 🚀 사용 방법

### 기본 사용법

```bash
python code_assistant.py [명령] [파일/폴더 경로] [옵션]
```

---

## 📖 명령어 예제

### 1. 파일 분석

```bash
# 기본 분석
python code_assistant.py analyze app.py

# 특정 질문과 함께
python code_assistant.py analyze app.py -q "이 코드의 보안 이슈는?"
python code_assistant.py analyze app.py -q "성능을 개선하려면?"
python code_assistant.py analyze app.py -q "이 함수는 어떻게 작동하나요?"
```

**출력 예시:**
```
📖 Reading: app.py
🤖 AI 분석 중...

이 Flask 앱의 주요 보안 이슈:
1. debug=True 모드 사용 (매우 위험!)
2. API 키 로그 노출
3. CORS 미적용
...
```

---

### 2. 프로젝트 전체 분석

```bash
# 현재 디렉토리 분석
python code_assistant.py analyze-dir .

# 특정 폴더 분석
python code_assistant.py analyze-dir ./src

# 특정 폴더와 질문을 함께
python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2/op-e2e/ -q "Slashing관련 테스트와 rat관련 테스트의 차이점을 분석해주세요"

python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2/docs-study/AdvancedSlash/ -q "여기 폴더 문서를 읽고 /Users/harvey/Desktop/onther/event/migration/ton-staking-v2 여기 폴더에 제대로 개발됬는지 확인해줘"

# 본인의 프로젝트 폴더에서
python /Users/harvey/Desktop/personal/aiAPIcall/code_assistant.py analyze-dir .

# 질문과 함께
python code_assistant.py analyze-dir . -q "이 프로젝트의 아키텍처는 어떤가요?"
```

**출력 예시:**
```
📁 Analyzing directory: .

프로젝트 구조:
📁 static/
  📁 css/
    📄 style.css (7.2KB)
  📁 js/
    📄 app.js (9.4KB)
📁 templates/
  📄 index.html (3.8KB)
📄 app.py (2.9KB)
...

🤖 AI 분석 중...

프로젝트 분석:
1. Flask 기반 웹 애플리케이션
2. AI 채팅 인터페이스 구현
3. 프론트엔드: Vanilla JS + CSS
...
```

---

### 3. 코드 리뷰

```bash
# 전문가 관점의 리뷰
python code_assistant.py review app.py
python code_assistant.py review static/js/app.js
```

**출력 예시:**
```
🔍 Reviewing: app.py

🤖 AI 코드 리뷰 중...

코드 리뷰:

✅ 좋은 점:
- 명확한 함수 분리
- 에러 처리 구현

⚠️ 개선 필요:
1. debug=True 제거 (보안 이슈)
   현재: app.run(debug=True, ...)
   개선: app.run(debug=False, ...)
   
2. 입력 검증 추가
   ...
```

---

### 4. 코드 리팩토링

```bash
# 기본 리팩토링
python code_assistant.py refactor app.py

# 특정 지시사항과 함께
python code_assistant.py refactor app.py -i "함수를 더 작게 분리해줘"
python code_assistant.py refactor app.py -i "타입 힌트를 추가해줘"
python code_assistant.py refactor app.py -i "async/await로 변경해줘"
```

**출력 예시:**
```
🔧 Refactoring: app.py

🤖 AI 리팩토링 중...

리팩토링된 코드:

```python
# 개선된 코드...
```

주요 변경사항:
1. 함수 분리: get_ai_client() 추가
2. 에러 처리 강화
3. 타입 힌트 추가
...
```

---

### 5. 코드 설명

```bash
# 전체 파일 설명
python code_assistant.py explain app.py

# 특정 라인만 설명
python code_assistant.py explain app.py --lines 10 30
python code_assistant.py explain static/js/app.js --lines 50 100
```

**출력 예시:**
```
📚 Explaining: app.py

🤖 AI 설명 중...

코드 설명:

이 코드는 Flask 웹 서버를 구현합니다:

1. AIService 클래스:
   - OpenAI 클라이언트 초기화
   - API 키와 베이스 URL 설정
   
2. chat_stream 메서드:
   - 스트리밍 방식으로 AI 응답 생성
   - Server-Sent Events (SSE) 사용
...
```

---

### 6. 버그 찾기

```bash
python code_assistant.py bugs app.py
python code_assistant.py bugs static/js/app.js
```

**출력 예시:**
```
🐛 Finding bugs in: app.py

🤖 AI 버그 찾는 중...

발견된 문제:

1. 🔴 보안 취약점 (라인 75)
   문제: debug=True 모드 사용
   위험: 원격 코드 실행 가능
   수정: debug=False로 변경
   
2. 🟡 예외 처리 누락 (라인 45)
   문제: API 호출 실패 시 처리 없음
   수정: try-except 추가
...
```

---

### 7. 테스트 생성

```bash
python code_assistant.py test app.py
python code_assistant.py test ai.py
```

---

### 8. 코드 직접 수정

```bash
# 특정 지시사항으로 파일 수정
python code_assistant.py apply app.py -q "API 키를 환경 변수에서 읽어오도록 수정해줘"

# 백업 없이 바로 수정
python code_assistant.py apply app.py -q "코드 스타일 정리해줘" --no-backup
```

**동작 방식:**
1. 원본 파일을 `app.py.bak`으로 백업합니다.
2. AI가 요청에 따라 코드를 수정합니다.
3. 원본 파일(`app.py`)을 수정된 코드로 덮어씁니다.
4. 변경 이력이 `analysis/` 폴더에 `apply_...md` 형태로 저장됩니다.

**출력 예시:**
```
🧪 Generating tests for: app.py

🤖 AI 테스트 생성 중...

생성된 테스트 코드:

```python
import pytest
from app import AIService

def test_ai_service_initialization():
    """AIService 초기화 테스트"""
    service = AIService()
    assert service.api_key is not None
    assert service.base_url == ""

def test_chat_stream_with_valid_input():
    """정상 입력으로 스트리밍 테스트"""
    ...
```
```

---

## 💡 실전 사용 예제

### 시나리오 1: 새 프로젝트 시작

```bash
# 1. 프로젝트 구조 파악
python code_assistant.py analyze-dir .

# 2. 주요 파일 분석
python code_assistant.py analyze app.py

# 3. 코드 리뷰
python code_assistant.py review app.py
```

---

### 시나리오 2: 버그 수정

```bash
# 1. 버그 찾기
python code_assistant.py bugs app.py

# 2. 특정 부분 설명 듣기
python code_assistant.py explain app.py --lines 45 60

# 3. 리팩토링
python code_assistant.py refactor app.py -i "버그를 수정하고 에러 처리를 강화해줘"
```

---

### 시나리오 3: 코드 품질 향상

```bash
# 1. 코드 리뷰
python code_assistant.py review app.py

# 2. 리팩토링
python code_assistant.py refactor app.py

# 3. 테스트 생성
python code_assistant.py test app.py
```

---

### 시나리오 4: 레거시 코드 이해

```bash
# 1. 전체 구조 파악
python code_assistant.py analyze-dir ./legacy_code

# 2. 주요 파일 설명
python code_assistant.py explain legacy_code/main.py

# 3. 특정 부분 질문
python code_assistant.py analyze legacy_code/main.py -q "이 함수는 왜 이렇게 복잡한가요?"
```

---

## 🎯 웹 인터페이스 vs Code Assistant

| 기능 | 웹 인터페이스 | Code Assistant |
|------|--------------|----------------|
| **용도** | 일반 채팅, 질문 | 코드 개발, 분석 |
| **코드 분석** | ❌ | ✅ 전문화 |
| **프로젝트 구조** | ❌ | ✅ 자동 파악 |
| **파일 읽기** | ❌ | ✅ 자동 |
| **코드 리뷰** | ⚙️ 수동 복붙 | ✅ 자동 |
| **리팩토링** | ⚙️ 수동 복붙 | ✅ 자동 |
| **테스트 생성** | ⚙️ 수동 복붙 | ✅ 자동 |
| **사용 편의성** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **개발 효율** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🔧 고급 사용법

# 다른 모델로 명시해서 사용하고 싶을 때
python code_assistant.py analyze app.py -m gpt-5.2-pro

# 기본 모델 사용 ( .env의 AI_MODEL 설정값 )
python code_assistant.py analyze app.py
```

---

### 📁 분석 결과 확인 (자동 저장)

분석 결과는 별도의 명령 없이도 `analysis/` 폴더에 **날짜별**로 자동 저장됩니다.

```bash
# 저장 구조 예시
analysis/
└── 2026-02-02/
    ├── analyze_app_20260202_223037.md
    └── review_main_20260202_223145.md
```

#### 저장 관련 옵션

```bash
# 저장하지 않고 화면에 출력만 하기
python code_assistant.py analyze app.py --no-save

# 다른 폴더에 저장하기
python code_assistant.py analyze app.py --save-dir ./my_results
```

---

### 💾 수동 출력 저장 (선택 사항)

자동 저장 외에 특정 파일명으로 직접 저장하고 싶을 때 사용합니다.

```bash
# 분석 결과를 특정 파일로 저장
python code_assistant.py analyze app.py > custom_analysis.md

# 리팩토링 결과를 파이썬 파일로 저장
python code_assistant.py refactor app.py > refactored_app.py
```

---

### 여러 파일 분석 (스크립트)

```bash
#!/bin/bash
# analyze_all.sh

for file in *.py; do
    echo "Analyzing $file..."
    python code_assistant.py analyze "$file" > "analysis_$file.md"
done
```

---

## 🚀 빠른 시작

```bash
# 1. 현재 프로젝트 분석
python code_assistant.py analyze-dir .

# 2. 주요 파일 리뷰
python code_assistant.py review app.py

# 3. 버그 찾기
python code_assistant.py bugs app.py
```

---

## 💡 팁

1. **프로젝트 시작 시**: `analyze-dir`로 전체 구조 파악
2. **코드 작성 후**: `review`로 품질 체크
3. **버그 발생 시**: `bugs`로 문제 찾기
4. **리팩토링 필요 시**: `refactor`로 개선
5. **코드 이해 필요 시**: `explain`으로 설명 듣기
6. **테스트 작성 시**: `test`로 자동 생성

---

**코드 개발이 훨씬 쉬워집니다! 🚀**
