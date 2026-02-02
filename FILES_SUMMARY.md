# 📂 Project Files Summary

이 프로젝트의 주요 파일들에 대한 기능 및 용도 정리입니다.

## 🛠️ 핵심 도구 (Main Tools)
- **`code_assistant.py`**: **프로젝트의 핵심 도구.** AI를 이용한 코드 분석, 리뷰, 리팩토링 및 직접 수정(`apply`) 기능을 제공하는 CLI 프로그램입니다.
- **`CODE_ASSISTANT_GUIDE.md`**: `code_assistant.py` 사용법을 상세히 설명하는 가이드 문서입니다.

## 🧪 예제 (`example/`)
- **`example/example.py`**: 가장 기본적인 AI 호출 예제입니다.
- **`example/list_models.py`**: 현재 사용 가능한 AI 모델 리스트를 확인하는 스크립트입니다.
- **`example/test_apply.py`**: `code_assistant.py`의 `apply` 명령어를 테스트하기 위한 연습용 파일입니다.

## 📦 레거시 및 기타 (`legacy/`)
- 안쓰는 파일들을 `legacy/` 폴더로 이동하여 정리했습니다.
- **`legacy/`**: 웹 인터페이스(`app.py` 등), 이전 테스트용 스크립트(`simple_call.py` 등), 예전 문서들.
- **`legacy/example/`**: 잘 사용하지 않는 토큰 체크 및 디버깅용 스크립트들.

## 📚 기반 파일
- **`ai.py`**: AI API 호출을 위한 기반 로직이 담긴 클래스 모듈입니다.
- **`PROJECT_SUMMARY.md` / **`README.md`**: 프로젝트 전체 개요 정보입니다.
- **`.env`**: API 키 및 환경 변수 설정 파일.
- **`requirements.txt`**: 프로젝트 실행에 필요한 라이브러리 목록입니다.
