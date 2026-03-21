import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ==============================
# 💬 CHAT (OPENROUTER)
# ==============================
def chat_with_ai(messages):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Todo AI App"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": messages,
            },
            timeout=15
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        data = response.json()

        if response.status_code == 200:
            return data["choices"][0]["message"]["content"]

        if "error" in data:
            return f"AI Error: {data['error']['message']}"

        return "AI failed"

    except Exception as e:
        print("ERROR:", str(e))
        return "Fallback active 🚀"

# ==============================
# ✨ GENERATE TODO
# ==============================
def generate_todo(text: str):
    prompt = f"""
    Convert into JSON:
    "{text}"

    Format:
    {{
      "title": "",
      "description": "",
      "priority": "low|medium|high"
    }}
    """

    res = chat_with_ai([
        {"role": "user", "content": prompt}
    ])

    try:
        return json.loads(res)
    except:
        return {
            "title": text,
            "description": f"Task: {text}",
            "priority": "medium"
        }


# ==============================
# 📊 PRIORITY
# ==============================
def predict_priority(title: str):
    prompt = f"""
    Decide priority:
    "{title}"

    Only return: low, medium, high
    """

    res = chat_with_ai([
        {"role": "user", "content": prompt}
    ])

    res = res.strip().lower()

    if res not in ["low", "medium", "high"]:
        return "medium"

    return res