import os
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from openai import OpenAI
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

app = Flask(__name__)

class AIService:
    def __init__(self):
        self.default_api_key = os.getenv("AI_API_KEY")
        self.base_url = os.getenv("AI_BASE_URL")
        
        if not self.default_api_key or self.default_api_key == "your_api_key_here":
            raise ValueError("AI_API_KEY must be set in .env file")
        if not self.base_url:
            raise ValueError("AI_BASE_URL must be set in .env file")
            
        # 모델별 키 매핑 미리 정의 (필요 시)
        # 예: AI_API_KEY_QWEN3_235B 등으로 환경변수를 설정해두면 개별 적용됨
    
    def _get_client_for_model(self, model_name):
        """모델에 최적인 API 키로 클라이언트 생성"""
        # 모델명에서 특수문자 제거하고 대문자로 변환 (예: qwen3-235b -> QWEN3_235B)
        env_suffix = model_name.replace("-", "_").replace(".", "_").upper()
        specific_key = os.getenv(f"AI_API_KEY_{env_suffix}")
        
        # 특정 그룹 키 (예: GPT 계열)
        if "gpt" in model_name.lower() or "opus" in model_name.lower():
            gpt_key = os.getenv("AI_API_KEY_GPT_OPUS")
            if gpt_key: specific_key = gpt_key
            
        key = specific_key or self.default_api_key
        return OpenAI(api_key=key, base_url=self.base_url)
    
    def get_available_models(self):
        """설정된 모든 API 키를 사용하여 접근 가능한 모든 모델 목록 조회"""
        all_models = set()
        keys_to_try = {self.default_api_key}
        
        # 환경 변수에서 모든 AI_API_KEY_ 로 시작하는 키 수집
        for key, value in os.environ.items():
            if key.startswith("AI_API_KEY_") and value:
                keys_to_try.add(value)
        
        for key in keys_to_try:
            if not key or key == "your_api_key_here": continue
            try:
                client = OpenAI(api_key=key, base_url=self.base_url)
                models = client.models.list()
                for model in models.data:
                    all_models.add(model.id)
            except Exception as e:
                print(f"Error fetching models for key {key[:10]}...: {e}")
        
        # 만약 API 호출로 가져온 모델이 없으면 환경변수에서 기본 세트 반환
        if not all_models:
            default_models = os.getenv("DEFAULT_MODELS", "")
            return [m.strip() for m in default_models.split(",") if m.strip()]
            
        return sorted(list(all_models))
    
    def chat_stream(self, messages, model="qwen3-235b"):
        """스트리밍 방식으로 응답"""
        try:
            client = self._get_client_for_model(model)
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            yield f"\n\n❌ Error ({model}): {str(e)}"

ai_service = AIService()

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/api/models', methods=['GET'])
def get_models():
    """사용 가능한 모델 목록 반환"""
    models = ai_service.get_available_models()
    return jsonify({"models": models})

@app.route('/api/chat', methods=['POST'])
def chat():
    """채팅 API - 스트리밍 응답"""
    data = request.json
    messages = data.get('messages', [])
    model = data.get('model', 'qwen3-235b')
    
    def generate():
        for content in ai_service.chat_stream(messages, model):
            yield f"data: {json.dumps({'content': content})}\n\n"
        yield "data: [DONE]\n\n"
    
    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )

@app.route('/api/health', methods=['GET'])
def health():
    """헬스 체크"""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    print("🚀 Starting Tokamak AI Chat Interface...")
    print("📡 Server running at: http://localhost:5000")
    print("🔑 Using API Key:", os.getenv("AI_API_KEY")[:10] + "..." if os.getenv("AI_API_KEY") else "NOT SET")
    app.run(debug=True, port=5000, threaded=True)
