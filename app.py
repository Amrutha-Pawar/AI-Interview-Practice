from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

# 1️⃣ CREATE FLASK APP FIRST
app = Flask(__name__)
CORS(app)

# 2️⃣ OPTIONAL HOME ROUTE (FOR TESTING)
@app.route("/")
def home():
    return "Backend is running"

# 3️⃣ EVALUATION ROUTE
@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json

    role = data.get("role", "")
    question = data.get("question", "")
    answer = data.get("answer", "")

    prompt = f"""
You are a strict interview evaluator.

ROLE: {role}

QUESTION:
{question}

EXPECTED ANSWER SHOULD INCLUDE:
- Clear definition
- Key concepts
- Correct technical terminology
- Example (if applicable)

CANDIDATE ANSWER:
{answer}

EVALUATION RULES:
- Penalize missing concepts
- Avoid generic praise
- Be factual and specific

Return response in EXACT format:

Score: X/10
Correct Points:
- ...
Missing / Weak Points:
- ...
Improved Answer:
...
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True
    )

    return jsonify({
        "feedback": result.stdout.strip()
    })

# 4️⃣ RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
