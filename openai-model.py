# https://github.com/openai/openai-python

import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# API 키를 환경 변수에서 가져옵니다.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

# OpenAI 클라이언트 인스턴스 생성
client = OpenAI(api_key=api_key)

# 모델 목록을 조회하는 함수
def list_models(client):
    response = client.models.list()
    models = response.data
    return models

# 1) 모델 목록을 가져와서 출력
models = list_models(client)
print("Available Models:")
for model in models:
    print(model.id)

# ChatCompletion API 호출
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

# 2) 응답 출력
print("\nChat Response:")
print(response.choices[0].message.content)