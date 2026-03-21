from sqlalchemy.orm import Session
from app.models.chat_model import Chat
from app.services.ai_service import chat_with_ai


def handle_chat(user_id, message, db: Session):

    print("STEP 1: saving user message")

    user_msg = Chat(
        user_id=user_id,
        role="user",
        content=message
    )
    db.add(user_msg)
    db.commit()
    db.refresh(user_msg)

    print("STEP 2: fetching history")

    history = (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.id.asc())
        .all()
    )

    messages = [
        {"role": chat.role, "content": chat.content}
        for chat in history
    ]

    print("STEP 3: calling AI")

    ai_response = chat_with_ai(messages)

    print("AI RESPONSE:", ai_response)

    print("STEP 4: saving AI response")

    ai_msg = Chat(
        user_id=user_id,
        role="assistant",
        content=ai_response
    )
    db.add(ai_msg)
    db.commit()
    db.refresh(ai_msg)

    return ai_response