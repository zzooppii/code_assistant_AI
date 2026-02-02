#!/usr/bin/env python3
"""
Tokamak AI Code Assistant with Auto-Save
코드 분석 결과를 자동으로 저장하는 기능 추가
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

class CodeAssistant:
    def __init__(self, model=None, save_dir=None):
        self.api_key = os.getenv("AI_API_KEY")
        # print("api_key", self.api_key)
        self.base_url = os.getenv("AI_BASE_URL")
        self.model = model or os.getenv("AI_MODEL")
        # print("model", self.model)
        
        # 저장 디렉토리 설정
        if save_dir:
            base_save_dir = Path(save_dir)
        else:
            # 기본: 현재 스크립트 위치의 analysis 폴더
            script_dir = Path(__file__).parent
            base_save_dir = script_dir / "analysis"
        
        # 날짜별 폴더 생성 (예: 2026-02-02)
        date_folder = datetime.now().strftime("%Y-%m-%d")
        self.save_dir = base_save_dir / date_folder
        
        # 디렉토리 생성 (상위 디렉토리 포함)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        
        if not self.api_key:
            raise ValueError("AI_API_KEY must be set in .env file")
        if not self.base_url:
            raise ValueError("AI_BASE_URL must be set in .env file")
            
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.current_output = []  # 출력 내용 저장용
    
    def _print_and_save(self, text, end='\n'):
        """출력하면서 동시에 저장"""
        print(text, end=end, flush=True)
        self.current_output.append(text + end)
    
    def _save_to_file(self, filename, content=None):
        """파일로 저장"""
        filepath = self.save_dir / filename
        
        if content is None:
            content = ''.join(self.current_output)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def read_file(self, filepath):
        """파일 읽기"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"
    
    def get_project_structure(self, directory, max_depth=3, current_depth=0):
        """프로젝트 구조 가져오기"""
        if current_depth >= max_depth:
            return ""
        
        structure = []
        try:
            path = Path(directory)
            items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
            
            for item in items:
                if item.name.startswith('.') or item.name in ['node_modules', '__pycache__', 'venv', '.venv', 'dist', 'build']:
                    continue
                
                indent = "  " * current_depth
                if item.is_dir():
                    structure.append(f"{indent}📁 {item.name}/")
                    sub_structure = self.get_project_structure(item, max_depth, current_depth + 1)
                    if sub_structure:
                        structure.append(sub_structure)
                else:
                    size = item.stat().st_size
                    size_str = self._format_size(size)
                    structure.append(f"{indent}📄 {item.name} ({size_str})")
        except Exception as e:
            structure.append(f"Error: {e}")
        
        return "\n".join(structure)
    
    def _format_size(self, size):
        """파일 크기 포맷팅"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f}{unit}"
            size /= 1024.0
        return f"{size:.1f}TB"
    
    def analyze_file(self, filepath, question=None, save=True):
        """파일 분석"""
        self.current_output = []
        
        self._print_and_save(f"📖 Reading: {filepath}")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        prompt = f"""다음 코드를 분석해주세요:

파일: {filepath}

```
{code}
```

"""
        if question:
            prompt += f"\n특히 다음에 대해 답변해주세요: {question}"
        else:
            prompt += """
다음 항목들을 분석해주세요:
1. 코드의 주요 기능과 목적
2. 코드 품질 (가독성, 유지보수성)
3. 잠재적인 버그나 개선점
4. 베스트 프랙티스 준수 여부
5. 성능 최적화 제안
"""
        
        self._print_and_save("\n🤖 AI 분석 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"analyze_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 분석 결과 저장: {saved_path}")
    
    def analyze_directory(self, directory, question=None, save=True):
        """디렉토리 전체 분석"""
        self.current_output = []
        
        self._print_and_save(f"📁 Analyzing directory: {directory}\n")
        
        structure = self.get_project_structure(directory)
        
        # 주요 파일들 읽기
        code_files = []
        for ext in ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rs', '.sol']:
            for filepath in Path(directory).rglob(f'*{ext}'):
                if any(exclude in str(filepath) for exclude in ['.venv', 'node_modules', '__pycache__']):
                    continue
                if filepath.stat().st_size < 50000:  # 50KB 이하만
                    code_files.append(filepath)
        
        files_content = ""
        for filepath in code_files[:10]:  # 최대 10개 파일
            content = self.read_file(filepath)
            if not content.startswith("Error"):
                files_content += f"\n\n### {filepath.name}\n```\n{content[:2000]}\n```\n"
        
        prompt = f"""다음 프로젝트를 분석해주세요:

프로젝트 경로: {directory}

프로젝트 구조:
```
{structure}
```

주요 파일들:
{files_content}

"""
        if question:
            prompt += f"\n특히 다음에 대해 답변해주세요: {question}"
        else:
            prompt += """
다음 항목들을 분석해주세요:
1. 프로젝트의 전체적인 구조와 아키텍처
2. 사용된 기술 스택
3. 코드 품질과 일관성
4. 개선 제안사항
5. 보안 이슈나 잠재적 문제점
"""
        
        self._print_and_save("\n🤖 AI 분석 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            dir_name = Path(directory).name
            filename = f"analyze_dir_{dir_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 분석 결과 저장: {saved_path}")
    
    def review_code(self, filepath, save=True):
        """코드 리뷰"""
        self.current_output = []
        
        self._print_and_save(f"🔍 Reviewing: {filepath}\n")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        prompt = f"""다음 코드를 전문 개발자 관점에서 리뷰해주세요:

파일: {filepath}

```
{code}
```

다음 관점에서 리뷰해주세요:
1. 코드 스타일과 컨벤션
2. 잠재적 버그
3. 성능 이슈
4. 보안 취약점
5. 테스트 가능성
6. 구체적인 개선 제안 (코드 예시 포함)

리뷰는 건설적이고 구체적으로 해주세요.
"""
        
        self._print_and_save("🤖 AI 코드 리뷰 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"review_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 리뷰 결과 저장: {saved_path}")
    
    def refactor_code(self, filepath, instruction=None, save=True):
        """코드 리팩토링"""
        self.current_output = []
        
        self._print_and_save(f"🔧 Refactoring: {filepath}\n")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        prompt = f"""다음 코드를 리팩토링해주세요:

파일: {filepath}

```
{code}
```

"""
        if instruction:
            prompt += f"\n리팩토링 요구사항: {instruction}\n"
        else:
            prompt += """
다음 원칙에 따라 리팩토링해주세요:
1. 가독성 향상
2. 중복 코드 제거
3. 함수/클래스 분리
4. 네이밍 개선
5. 성능 최적화

리팩토링된 전체 코드를 제공해주세요.
"""
        
        self._print_and_save("🤖 AI 리팩토링 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"refactor_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 리팩토링 결과 저장: {saved_path}")
    
    def explain_code(self, filepath, line_start=None, line_end=None, save=True):
        """코드 설명"""
        self.current_output = []
        
        self._print_and_save(f"📚 Explaining: {filepath}\n")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        if line_start and line_end:
            lines = code.split('\n')
            code = '\n'.join(lines[line_start-1:line_end])
            self._print_and_save(f"Lines {line_start}-{line_end}:\n")
        
        prompt = f"""다음 코드를 초보자도 이해할 수 있도록 자세히 설명해주세요:

```
{code}
```

다음을 포함해서 설명해주세요:
1. 전체적인 동작 방식
2. 각 부분의 역할
3. 사용된 개념/패턴
4. 주의할 점
5. 실제 사용 예시
"""
        
        self._print_and_save("🤖 AI 설명 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"explain_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 설명 결과 저장: {saved_path}")
    
    def find_bugs(self, filepath, save=True):
        """버그 찾기"""
        self.current_output = []
        
        self._print_and_save(f"🐛 Finding bugs in: {filepath}\n")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        prompt = f"""다음 코드에서 버그나 잠재적 문제를 찾아주세요:

파일: {filepath}

```
{code}
```

다음을 찾아주세요:
1. 논리적 오류
2. 예외 처리 누락
3. 메모리 누수 가능성
4. 경쟁 조건 (race condition)
5. 보안 취약점
6. 엣지 케이스 미처리

각 문제에 대해:
- 문제가 있는 코드 라인
- 문제 설명
- 수정 방법
을 제시해주세요.
"""
        
        self._print_and_save("🤖 AI 버그 찾는 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"bugs_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 버그 분석 결과 저장: {saved_path}")
    
    def generate_tests(self, filepath, save=True):
        """테스트 코드 생성"""
        self.current_output = []
        
        self._print_and_save(f"🧪 Generating tests for: {filepath}\n")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        ext = Path(filepath).suffix
        lang_map = {
            '.py': 'pytest',
            '.js': 'Jest',
            '.ts': 'Jest',
            '.java': 'JUnit',
            '.go': 'testing package',
            '.sol': 'Hardhat/Foundry'
        }
        test_framework = lang_map.get(ext, 'appropriate testing framework')
        
        prompt = f"""다음 코드에 대한 테스트 코드를 작성해주세요:

파일: {filepath}

```
{code}
```

{test_framework}를 사용하여:
1. 단위 테스트 (unit tests)
2. 엣지 케이스 테스트
3. 에러 케이스 테스트
4. 통합 테스트 (필요시)

완전하고 실행 가능한 테스트 코드를 제공해주세요.
"""
        
        self._print_and_save("🤖 AI 테스트 생성 중...\n")
        self._stream_response(prompt)
        
        # 저장
        if save:
            filename = f"test_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = self._save_to_file(filename)
            print(f"\n\n💾 테스트 코드 저장: {saved_path}")
    
    def apply_fix(self, filepath, instruction, no_backup=False, save=True):
        """AI 지시사항에 따라 코드 수정 및 적용"""
        self.current_output = []
        
        self._print_and_save(f"🛠️ Applying fix to: {filepath}")
        code = self.read_file(filepath)
        
        if code.startswith("Error"):
            self._print_and_save(f"❌ {code}")
            return
        
        prompt = f"""다음 코드를 사용자의 지시사항에 따라 수정해주세요.
수정된 **전체 코드**만 코드 블록(```) 안에 넣어서 응답해주세요. 불필요한 설명은 제외해주세요.

파일: {filepath}

지시사항: {instruction}

현재 코드:
```
{code}
```
"""
        
        self._print_and_save("🤖 AI가 코드를 수정 중...\n")
        
        # 스트리밍 대신 전체 응답을 한꺼번에 받아서 처리 (코드 추출을 위해)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            full_response = response.choices[0].message.content
            
            # 코드 블록 추출
            new_code = self._extract_code(full_response)
            
            if not new_code or new_code.strip() == code.strip():
                self._print_and_save("⚠️ 수정된 내용이 없거나 코드를 추출할 수 없습니다.")
                return
            
            # 백업 생성
            if not no_backup:
                backup_path = Path(filepath).with_suffix(Path(filepath).suffix + ".bak")
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                self._print_and_save(f"📦 백업 생성됨: {backup_path}")
            
            # 파일 쓰기
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            self._print_and_save(f"✅ 코드가 성공적으로 수정되었습니다: {filepath}")
            
            # 변경 사항 요약 저장
            if save:
                filename = f"apply_{Path(filepath).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                summary = f"# Code Change Summary\n\n**File:** {filepath}\n**Instruction:** {instruction}\n\n## AI Response\n{full_response}"
                saved_path = self._save_to_file(filename, content=summary)
                print(f"💾 변경 이력 저장: {saved_path}")
                
        except Exception as e:
            self._print_and_save(f"❌ Error: {e}")

    def _extract_code(self, text):
        """텍스트에서 코드 블럭 추출"""
        import re
        # ```python ... ``` 또는 ``` ... ``` 형태 추출
        pattern = r"```(?:[a-zA-Z0-9]+)?\n?(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        
        if matches:
            # 가장 긴 코드 블록 반환 (보통 전체 코드)
            return max(matches, key=len).strip()
        
        # 코드 블록이 없으면 텍스트 전체(설명이 없을 것을 기대)
        return text.strip()

    def _stream_response(self, prompt):
        """스트리밍 응답"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    self._print_and_save(content, end='')
            self._print_and_save("\n")
        except Exception as e:
            self._print_and_save(f"❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Tokamak AI Code Assistant - 코드 분석 및 개발 도우미 (자동 저장 기능)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:

  # 파일 분석 (자동 저장)
  python code_assistant.py analyze app.py
  
  # 다른 프로젝트 분석
  python code_assistant.py analyze-dir /Users/harvey/Desktop/onther/event/migration/ton-staking-v2
  
  # 저장 위치 지정
  python code_assistant.py analyze app.py --save-dir ./my_analysis
  
  # 저장하지 않고 출력만
  python code_assistant.py analyze app.py --no-save
  
  # 코드 리뷰
  python code_assistant.py review app.py
        """
    )
    
    parser.add_argument(
        'command',
        choices=['analyze', 'analyze-dir', 'review', 'refactor', 'explain', 'bugs', 'test', 'apply'],
        help='실행할 명령'
    )
    
    parser.add_argument(
        'path',
        help='분석할 파일 또는 디렉토리 경로'
    )
    
    parser.add_argument(
        '-q', '--question',
        help='특정 질문 (analyze, analyze-dir에서 사용)'
    )
    
    parser.add_argument(
        '-i', '--instruction',
        help='리팩토링 지시사항 (refactor에서 사용)'
    )
    
    parser.add_argument(
        '--lines',
        nargs=2,
        type=int,
        metavar=('START', 'END'),
        help='분석할 라인 범위 (explain에서 사용)'
    )
    
    parser.add_argument(
        '-m', '--model',
        default=None,
        help='사용할 AI 모델 (기본값: .env의 AI_MODEL)'
    )
    
    parser.add_argument(
        '--save-dir',
        default=None,
        help='분석 결과 저장 디렉토리 (기본값: ./analysis)'
    )
    
    parser.add_argument(
        '--no-save',
        action='store_true',
        help='파일로 저장하지 않고 출력만'
    )
    
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='수정 전 백업 파일을 생성하지 않음'
    )
    
    args = parser.parse_args()
    
    try:
        assistant = CodeAssistant(model=args.model, save_dir=args.save_dir)
        save = not args.no_save
        
        print(f"📁 분석 결과 저장 위치: {assistant.save_dir}\n")
        
        if args.command == 'analyze':
            assistant.analyze_file(args.path, args.question, save=save)
        elif args.command == 'analyze-dir':
            assistant.analyze_directory(args.path, args.question, save=save)
        elif args.command == 'review':
            assistant.review_code(args.path, save=save)
        elif args.command == 'refactor':
            assistant.refactor_code(args.path, args.instruction, save=save)
        elif args.command == 'explain':
            if args.lines:
                assistant.explain_code(args.path, args.lines[0], args.lines[1], save=save)
            else:
                assistant.explain_code(args.path, save=save)
        elif args.command == 'bugs':
            assistant.find_bugs(args.path, save=save)
        elif (args.command == 'test'):
            assistant.generate_tests(args.path, save=save)
        elif args.command == 'apply':
            if not args.question:
                print("❌ 'apply' 명령은 -q (질문/지시) 옵션이 필수입니다.", file=sys.stderr)
                sys.exit(1)
            assistant.apply_fix(args.path, args.question, no_backup=args.no_backup, save=save)
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
