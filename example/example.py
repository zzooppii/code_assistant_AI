import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url=os.getenv("AI_BASE_URL")
)

response = client.chat.completions.create(
    model="qwen3-coder-pro", # model to send to the proxy
    messages = [
        {
            "role": "user",
            "content": "안녕 넌 누구고 언제까지 학습한 모델이야?"
        }
    ]
)

print(response)