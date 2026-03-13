import requests
import json

API_KEY = "AIzaSyDZP-Tz2I1gTXseikrKQHc96qqOolqOGD8"

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

prompt = """
You are an interview evaluator.

Evaluate the following answer and give:
1. Score out of 10
2. Strengths
3. Improvements

Answer:
I am a computer science student with interest in web development.
"""

data = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

# Print AI response safely
print(result["candidates"][0]["content"]["parts"][0]["text"])
