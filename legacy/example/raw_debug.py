import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def raw_request():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    model = os.getenv("AI_MODEL")
    
    url = f"{base_url}/chat/completions"
    if "/v1" not in url:
        url = f"{base_url}/v1/chat/completions"
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": "hi"}]
    }
    
    print(f"Requesting URL: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {json.dumps(data)}")
    
    response = requests.post(url, headers=headers, json=data)
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    raw_request()
