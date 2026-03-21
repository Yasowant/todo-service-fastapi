from fastapi import APIRouter
from .auth_routes import router as auth_router
from .todo_routes import router as todo_router
from .ai_routes import router as ai_router

api_v1_router = APIRouter()

api_v1_router.include_router(auth_router)
api_v1_router.include_router(todo_router)
api_v1_router.include_router(ai_router)