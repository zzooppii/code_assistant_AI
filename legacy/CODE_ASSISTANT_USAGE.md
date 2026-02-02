# 🎯 Code Assistant 사용 가이드 (자동 저장 기능)

## ✅ 완성! 자동 저장 기능 추가

이제 **모든 분석 결과가 자동으로 `analysis/` 폴더에 저장**됩니다!

---

## 🚀 사용 방법

### 1. 현재 프로젝트 분석
```bash
cd /Users/harvey/Desktop/personal/aiAPIcall
python code_assistant.py analyze-dir .
```

**결과:**
- 터미널에 분석 결과 출력
- `analysis/analyze_dir_aiAPIcall_20260114_154217.md` 자동 저장 ✅

---

### 2. 다른 프로젝트 분석 (핵심!)
```bash
# ton-staking-v2 프로젝트 분석
python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2
```

**결과:**
- 터미널에 분석 결과 출력
- `analysis/analyze_dir_ton-staking-v2_20260114_154500.md` 자동 저장 ✅

---

### 3. 특정 파일 분석
```bash
# 현재 프로젝트의 파일
python code_assistant.py analyze app.py

# 다른 프로젝트의 파일
python code_assistant.py analyze /Users/harvey/Desktop/onther/event/migration/ton-staking-v2/contracts/Staking.sol
```

**결과:**
- `analysis/analyze_app_20260114_154217.md` 자동 저장 ✅
- `analysis/analyze_Staking_20260114_154600.md` 자동 저장 ✅

---

### 4. 특정 질문과 함께 분석
```bash
python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2 -q "이 프로젝트의 보안 이슈는?"
```

**결과:**
- 보안 이슈에 초점을 맞춘 분석
- `analysis/analyze_dir_ton-staking-v2_20260114_154700.md` 자동 저장 ✅

---

## 📁 저장 위치

### 기본 저장 위치
```
/Users/harvey/Desktop/personal/aiAPIcall/analysis/
```

모든 분석 결과가 여기에 저장됩니다!

### 저장 파일 이름 형식
```
[명령]_[파일/폴더명]_[날짜]_[시간].md

예시:
- analyze_app_20260114_154217.md
- analyze_dir_ton-staking-v2_20260114_154500.md
- review_Staking_20260114_154600.md
- bugs_app_20260114_154700.md
```

---

## 🎯 모든 명령어 (자동 저장)

### 1. 프로젝트 분석
```bash
python code_assistant.py analyze-dir /path/to/project
```

### 2. 파일 분석
```bash
python code_assistant.py analyze /path/to/file.py
```

### 3. 코드 리뷰
```bash
python code_assistant.py review /path/to/file.py
```

### 4. 버그 찾기
```bash
python code_assistant.py bugs /path/to/file.py
```

### 5. 리팩토링
```bash
python code_assistant.py refactor /path/to/file.py
```

### 6. 코드 설명
```bash
python code_assistant.py explain /path/to/file.py
```

### 7. 테스트 생성
```bash
python code_assistant.py test /path/to/file.py
```

**모든 명령어의 결과가 `analysis/` 폴더에 자동 저장됩니다!** ✅

---

## 🛠️ 고급 옵션

### 저장 위치 변경
```bash
# 다른 폴더에 저장
python code_assistant.py analyze app.py --save-dir ./my_analysis

# 결과: ./my_analysis/analyze_app_20260114_154217.md
```

### 저장하지 않고 출력만
```bash
# 파일로 저장하지 않음
python code_assistant.py analyze app.py --no-save
```

### 다른 모델 사용
```bash
# Qwen3-80B-Next (더 빠름)
python code_assistant.py analyze app.py -m qwen3-80b-next
```

---

## 💡 실전 예제

### 예제 1: ton-staking-v2 프로젝트 전체 분석
```bash
cd /Users/harvey/Desktop/personal/aiAPIcall

python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2
```

**결과:**
```
📁 분석 결과 저장 위치: /Users/harvey/Desktop/personal/aiAPIcall/analysis

📁 Analyzing directory: /Users/harvey/Desktop/onther/event/migration/ton-staking-v2

🤖 AI 분석 중...

[프로젝트 구조, 아키텍처, 기술 스택, 개선점 등 상세 분석...]

💾 분석 결과 저장: /Users/harvey/Desktop/personal/aiAPIcall/analysis/analyze_dir_ton-staking-v2_20260114_154500.md
```

---

### 예제 2: 특정 Solidity 파일 보안 분석
```bash
python code_assistant.py analyze /Users/harvey/Desktop/onther/event/migration/ton-staking-v2/contracts/Staking.sol -q "보안 취약점은?"
```

**결과:**
```
📁 분석 결과 저장 위치: /Users/harvey/Desktop/personal/aiAPIcall/analysis

📖 Reading: /Users/harvey/Desktop/onther/event/migration/ton-staking-v2/contracts/Staking.sol

🤖 AI 분석 중...

[보안 취약점 상세 분석...]

💾 분석 결과 저장: /Users/harvey/Desktop/personal/aiAPIcall/analysis/analyze_Staking_20260114_154600.md
```

---

### 예제 3: 여러 프로젝트 일괄 분석
```bash
#!/bin/bash
# analyze_all_projects.sh

projects=(
    "/Users/harvey/Desktop/onther/event/migration/ton-staking-v2"
    "/Users/harvey/Desktop/onther/another-project"
    "/Users/harvey/Desktop/onther/third-project"
)

for project in "${projects[@]}"; do
    echo "Analyzing $project..."
    python code_assistant.py analyze-dir "$project"
    echo "---"
done
```

**결과:**
- 모든 프로젝트 분석 결과가 `analysis/` 폴더에 저장됨
- 파일명으로 구분 가능

---

## 📊 저장된 파일 확인

### 저장된 파일 목록 보기
```bash
ls -lh analysis/
```

### 최근 분석 결과 보기
```bash
# 가장 최근 파일
ls -t analysis/ | head -1

# 내용 보기
cat analysis/$(ls -t analysis/ | head -1)
```

### VS Code에서 열기
```bash
code analysis/
```

---

## 🎯 요약

### ✅ 장점
1. **자동 저장** - 모든 분석 결과가 자동으로 저장됨
2. **체계적 관리** - 날짜/시간이 포함된 파일명으로 쉽게 찾기
3. **다른 프로젝트 분석** - 어디서든 분석 가능
4. **결과 보관** - 나중에 다시 확인 가능

### 📁 저장 위치
```
/Users/harvey/Desktop/personal/aiAPIcall/analysis/
```

### 🚀 사용 방법
```bash
# 기본 (자동 저장)
python code_assistant.py analyze-dir /path/to/project

# 저장 위치 변경
python code_assistant.py analyze-dir /path/to/project --save-dir ./my_analysis

# 저장하지 않음
python code_assistant.py analyze-dir /path/to/project --no-save
```

---

## 💡 팁

1. **프로젝트 분석 후 파일 확인**
   ```bash
   python code_assistant.py analyze-dir /path/to/project
   code analysis/  # VS Code에서 결과 확인
   ```

2. **특정 질문으로 여러 프로젝트 비교**
   ```bash
   python code_assistant.py analyze-dir /project1 -q "보안 이슈는?"
   python code_assistant.py analyze-dir /project2 -q "보안 이슈는?"
   # analysis/ 폴더에서 두 결과 비교
   ```

3. **정기적인 코드 품질 체크**
   ```bash
   # 매주 월요일 자동 실행 (cron)
   0 9 * * 1 cd /Users/harvey/Desktop/personal/aiAPIcall && python code_assistant.py analyze-dir /path/to/project
   ```

---

**이제 어떤 프로젝트든 쉽게 분석하고, 결과를 체계적으로 관리할 수 있습니다! 🚀✨**
