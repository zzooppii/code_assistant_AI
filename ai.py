#!/usr/bin/env python3
"""
Tokamak AI CLI Tool
명령줄에서 빠르게 AI와 대화할 수 있는 도구
"""

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

class TokamakAI:
    def __init__(self, model=None):
        self.api_key = os.getenv("AI_API_KEY")
        self.base_url = os.getenv("AI_BASE_URL")
        self.model = model or os.getenv("AI_MODEL")
        
        if not self.api_key:
            raise ValueError("AI_API_KEY must be set in .env file")
        if not self.base_url:
            raise ValueError("AI_BASE_URL must be set in .env file")
            
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
    
    def ask(self, question, stream=True):
        """단일 질문에 대한 답변"""
        try:
            if stream:
                return self._stream_response(question)
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": question}]
                )
                return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
    
    def _stream_response(self, question):
        """스트리밍 응답"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": question}],
            stream=True
        )
        
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response += content
        print()  # 줄바꿈
        return full_response
    
    def chat(self):
        """대화형 모드"""
        print(f"🤖 Tokamak AI Chat (Model: {self.model})")
        print("Type 'exit' or 'quit' to end the conversation.\n")
        
        messages = []
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                messages.append({"role": "user", "content": user_input})
                
                print("AI: ", end="", flush=True)
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    stream=True
                )
                
                full_response = ""
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        print(content, end="", flush=True)
                        full_response += content
                
                print("\n")
                messages.append({"role": "assistant", "content": full_response})
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Tokamak AI CLI Tool - AI와 명령줄에서 대화하기",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  # 단일 질문
  python ai.py "Python으로 웹 크롤러 만드는 방법"
  
  # 대화형 모드
  python ai.py --chat
  
  # 다른 모델 사용
  python ai.py --model qwen3-80b-next "블록체인이란?"
  
  # 스트리밍 없이 전체 응답 받기
  python ai.py --no-stream "간단한 시 하나 써줘"
        """
    )
    
    parser.add_argument(
        'question',
        nargs='?',
        help='AI에게 물어볼 질문'
    )
    
    parser.add_argument(
        '-c', '--chat',
        action='store_true',
        help='대화형 모드 시작'
    )
    
    parser.add_argument(
        '-m', '--model',
        default=None,
        help='사용할 AI 모델 (기본값: qwen3-235b)'
    )
    
    parser.add_argument(
        '--no-stream',
        action='store_true',
        help='스트리밍 없이 전체 응답 받기'
    )
    
    parser.add_argument(
        '--list-models',
        action='store_true',
        help='사용 가능한 모델 목록 표시'
    )
    
    args = parser.parse_args()
    
    try:
        ai = TokamakAI(model=args.model)
        
        if args.list_models:
            print("📋 Available models:")
            try:
                models = ai.client.models.list()
                for model in models.data:
                    print(f"  - {model.id}")
            except Exception as e:
                print(f"Error fetching models: {e}")
                print("  - qwen3-235b (default)")
                print("  - qwen3-80b-next")
            return
        
        if args.chat:
            ai.chat()
        elif args.question:
            print(f"🤔 Question: {args.question}\n")
            print("🤖 AI: ", end="" if not args.no_stream else "\n", flush=True)
            response = ai.ask(args.question, stream=not args.no_stream)
            if args.no_stream:
                print(response)
        else:
            parser.print_help()
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
