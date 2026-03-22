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
                "temperature": 0.3  # ✅ more predictable output
            },
            timeout=15
        )

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
# ✨ GENERATE TODO (UPDATED)
# ==============================
def generate_todo(text: str):
    prompt = f"""
    Convert the following into STRICT JSON.

    Text:
    "{text}"

    Rules:
    - Return ONLY valid JSON (no explanation)
    - Keys: title, description, priority, status
    - priority must be: low | medium | high
    - status must be: pending | in_progress | completed

    Example:
    {{
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "priority": "medium",
      "status": "pending"
    }}
    """

    res = chat_with_ai([
        {"role": "user", "content": prompt}
    ])

    try:
        parsed = json.loads(res)

        # ✅ safety fallback
        return {
            "title": parsed.get("title", text),
            "description": parsed.get("description", f"Task: {text}"),
            "priority": validate_priority(parsed.get("priority")),
            "status": validate_status(parsed.get("status"))
        }

    except Exception:
        return {
            "title": text,
            "description": f"Task: {text}",
            "priority": "medium",
            "status": "pending"
        }


# ==============================
# 📊 PRIORITY (SAFE)
# ==============================
def predict_priority(title: str):
    prompt = f"""
    Decide priority for:
    "{title}"

    Only return one word: low, medium, or high
    """

    res = chat_with_ai([
        {"role": "user", "content": prompt}
    ])

    return validate_priority(res)


# ==============================
# ✅ VALIDATORS (IMPORTANT 🔥)
# ==============================
def validate_priority(value):
    if not value:
        return "medium"

    value = value.strip().lower()
    return value if value in ["low", "medium", "high"] else "medium"


def validate_status(value):
    if not value:
        return "pending"

    value = value.strip().lower()
    return value if value in ["pending", "in_progress", "completed"] else "pending"