import os
import json
import urllib.request
from dotenv import load_dotenv

# 상위 디렉토리의 .env 파일을 로드하기 위해 경로 조정
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
load_dotenv(os.path.join(parent_dir, ".env"))

def check_token_usage(text_content):
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    # 모델도 환경변수에서 가져오거나 기본값 사용
    model = os.getenv("AI_MODEL")

    if not api_key or not base_url:
        print("Error: AI_API_KEY or AI_BASE_URL not found in .env")
        return

    # Remove /v1 suffix if present to get to root
    if base_url.endswith("/v1"):
        server_root = base_url[:-3]
    elif base_url.endswith("/v1/"):
        server_root = base_url[:-4]
    else:
        server_root = base_url

    token_url = f"{server_root}/utils/token_counter"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Payload: messages format is supported
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": text_content}
        ]
    }

    try:
        req = urllib.request.Request(
            token_url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            body = response.read().decode('utf-8')
            data = json.loads(body)
            
            print(f"--- Token Usage Check ---")
            print(f"Model: {data.get('model_used', model)}")
            print(f"Input Text: {text_content}")
            print(f"Total Tokens: {data.get('total_tokens')}")
            return data
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        print(f"Response: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_text = "API 목록에 있는 토큰 카운터 기능을 테스트합니다."
    check_token_usage(test_text)
