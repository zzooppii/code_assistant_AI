import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

def list_models_verbose():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    try:
        models = client.models.list()
        print("Available Models (Verbose):")
        for model in models:
            print(f"ID: {model.id}")
            # Try to print dict representation if possible
            try:
                print(f"Details: {model.model_dump_json(indent=2)}")
            except:
                print(f"Details: {model}")
                
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models_verbose()
