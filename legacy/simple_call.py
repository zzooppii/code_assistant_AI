import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

def get_ai_client():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    
    if not api_key or api_key == "your_api_key_here" or not base_url:
        print("Error: AI_API_KEY or AI_BASE_URL is not set in .env file.")
        return None
        
    return OpenAI(
        api_key=api_key,
        base_url=base_url
    )

def simple_chat(prompt, model=None):
    client = get_ai_client()
    if not client:
        return
        
    model = model or os.getenv("AI_MODEL")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    test_prompt = "너 한글은 이해해?"
    print(f"Sending prompt: {test_prompt}")
    result = simple_chat(test_prompt)
    print("\nAI Response:")
    print(result)
