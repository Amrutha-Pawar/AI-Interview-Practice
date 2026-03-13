from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENAI_API_KEY")

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.json
    role = data.get("role","")
    question = data.get("question","")
    answer = data.get("answer","")

    prompt = f"""
You are a strict interview evaluator.

ROLE: {role}

QUESTION:
{question}

EXPECTED ANSWER SHOULD INCLUDE:
- Clear definition
- Key concepts
- Correct technical terminology
- Example if applicable

CANDIDATE ANSWER:
{answer}

Return response in format:

Score: X/10
Correct Points:
- ...

Missing Points:
- ...

Improved Answer:
...
"""

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents":[
            {
                "parts":[{"text":prompt}]
            }
        ]
    }

    headers = {
        "Content-Type":"application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    result = response.json()

    feedback = result["candidates"][0]["content"]["parts"][0]["text"]

    return jsonify({"feedback": feedback})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)