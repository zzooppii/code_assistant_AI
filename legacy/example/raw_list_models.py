import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def raw_list_models():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    
    url = f"{base_url}/models"
    # if "/v1" not in url:
    #     url = f"{base_url}/v1/models"
        
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    raw_list_models()
