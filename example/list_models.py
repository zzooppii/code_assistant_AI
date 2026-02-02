import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def list_models():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    
    if not api_key or not base_url:
        print("Error: AI_API_KEY and AI_BASE_URL must be set in .env file")
        return
        
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    try:
        models = client.models.list()
        print("Available Models:")
        for model in models:
            print(f"- {model.id}")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
