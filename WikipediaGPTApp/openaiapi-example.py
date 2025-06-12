import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Napiši esej o veštačkoj inteligenciji."}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response['choices'][0]['message']['content'])
