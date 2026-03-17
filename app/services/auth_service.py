from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user_model import User
from app.utils.security import hash_password, verify_password
from app.services.token_service import create_access_token, create_refresh_token


def register_user(db: Session, name:str, email: str, password: str):

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access = create_access_token({"sub": str(user.id)})   # ✅ FIX
    refresh = create_refresh_token({"sub": str(user.id)}) # ✅ FIX

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }