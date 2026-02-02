#!/bin/bash

# Tokamak AI 웹 인터페이스 시작 스크립트

echo "🚀 Starting Tokamak AI Web Interface..."
echo ""

# 가상환경 활성화
if [ -d ".venv" ]; then
    echo "✅ Activating virtual environment..."
    source .venv/bin/activate
else
    echo "❌ Virtual environment not found!"
    echo "Please create one with: python -m venv .venv"
    exit 1
fi

# 필요한 패키지 확인
echo "📦 Checking dependencies..."
pip show flask > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️  Flask not found. Installing..."
    pip install -r requirements.txt
fi

# API 키 확인
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "Please create .env file with your API key"
    exit 1
fi

# 서버 시작
echo ""
echo "🌐 Starting web server..."
echo "📡 Open your browser and go to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
