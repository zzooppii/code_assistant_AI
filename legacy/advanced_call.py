import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

class AIService:
    def __init__(self):
        self.api_key = os.getenv("AI_API_KEY")
        self.base_url = os.getenv("AI_BASE_URL")
        self.model = os.getenv("AI_MODEL", "Qwen3-235b")
        
        if not self.api_key or self.api_key == "your_api_key_here" or not self.base_url:
            raise ValueError("AI_API_KEY and AI_BASE_URL must be set in .env file")
            
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def chat_stream(self, prompt, system_prompt="You are a helpful assistant."):
        """스트리밍 방식으로 결과를 출력하여 사용자 경험을 향상시킵니다."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            
            print(f"Assistant ({self.model}): ", end="", flush=True)
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
            print("\n")
            return full_response
        except Exception as e:
            print(f"\nError during streaming: {e}")
            return None

    def chat_with_history(self, messages):
        """대화 맥락(History)을 유지하며 대화합니다."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None

def main():
    try:
        ai = AIService()
        
        print("=== Tokamak AI Advanced Call Demo ===")
        print("1. Streaming Call")
        print("2. Multi-turn Chat (History)")
        choice = input("Select an option (1/2): ")
        
        if choice == "1":
            user_input = input("Enter your prompt: ")
            ai.chat_stream(user_input)
            
        elif choice == "2":
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
            print("Type 'exit' to quit.")
            while True:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    break
                
                messages.append({"role": "user", "content": user_input})
                reply = ai.chat_with_history(messages)
                
                if reply:
                    print(f"AI: {reply}")
                    messages.append({"role": "assistant", "content": reply})
                else:
                    break
                    
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
