from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user
from app.services.email_service import send_verification_email


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = register_user(db,user.name, user.email, user.password)

    await send_verification_email(user.email)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    tokens = login_user(db, user.email, user.password)

    return tokens

@router.post("/logout")
def logout():
    return{
        "message":"Logout successful.Please remove the token from client storage"
    }