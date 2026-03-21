from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.ai_service import generate_todo, predict_priority
from app.services.chat_service import handle_chat
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])


# 💬 ChatGPT-like
@router.post("/chat")
def chat(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        return {"reply": handle_chat(user.id, data["message"], db)}
    except Exception as e:
        print("FULL ERROR:", str(e))
        return {"error": str(e)}


# ✨ Auto-create todo
@router.post("/generate-todo")
def ai_generate(data: dict):
    return generate_todo(data["text"])


# 📊 Priority prediction
@router.post("/predict-priority")
def ai_priority(data: dict):
    return {"priority": predict_priority(data["title"])}