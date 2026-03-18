from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user
from app.services.email_service import send_verification_email
from app.utils.dependencies import get_current_user
from app.models.user_model import User


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

@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "is_verified": current_user.is_verified
    }