import subprocess

answer = "I am a computer science student interested in web development."

prompt = f"""
Evaluate this interview answer.
Give:
1. Score out of 10
2. Strengths
3. Improvements

Answer:
{answer}
"""

result = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt,
    text=True,
    encoding="utf-8",      # ✅ FIX
    errors="ignore",       # ✅ FIX
    capture_output=True
)

print(result.stdout)
