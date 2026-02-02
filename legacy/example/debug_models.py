import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def debug_call():
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_BASE_URL")
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    try:
        models = client.models.list()
        model_ids = [m.id for m in models]
        print(f"Detected models: {model_ids}")
        
        for m_id in model_ids:
            print(f"\nTrying model: {m_id}")
            try:
                response = client.chat.completions.create(
                    model=m_id,
                    messages=[{"role": "user", "content": "hi"}]
                )
                print(f"Success! Response: {response.choices[0].message.content}")
            except Exception as e:
                print(f"Failed for {m_id}: {e}")
                
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    debug_call()
