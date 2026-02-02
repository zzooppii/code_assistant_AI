import os
import json
import urllib.request
from dotenv import load_dotenv

# 상위 디렉토리의 .env 파일을 로드하기 위해 경로 조정
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
load_dotenv(os.path.join(parent_dir, ".env"))

def check_agent_activity():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")

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

    # Target Endpoint
    endpoint_url = f"{server_root}/agent/daily/activity"
    print(f"Target URL: {endpoint_url}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        req = urllib.request.Request(
            endpoint_url,
            headers=headers,
            method='GET'
        )
        
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            body = response.read().decode('utf-8')
            
            print(f"--- Agent Daily Activity Check ---")
            print(f"Status: {status}")
            
            try:
                data = json.loads(body)
                print(json.dumps(data, indent=2, ensure_ascii=False))
            except:
                print(body)
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        print(f"Response: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_agent_activity()
