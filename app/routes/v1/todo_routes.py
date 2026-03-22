from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoResponse
from app.services import todo_service
from app.utils.dependencies import get_current_user
from app.models.user_model import User
from app.services.ai_service import generate_todo

router = APIRouter(prefix="/todos", tags=["Todos"])


# 🔥 AI CREATE
@router.post("/ai", response_model=TodoResponse)
def create_todo_ai(
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        ai_data = generate_todo(data["text"])
        return todo_service.create_todo(db, ai_data, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 🔹 CREATE
@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return todo_service.create_todo(db, todo, current_user.id)


# 🔹 GET ALL
@router.get("/", response_model=list[TodoResponse])
def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return todo_service.get_all_todos(db, current_user.id)


# 🔹 GET ONE
@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = todo_service.get_todo(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# 🔹 UPDATE
@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: UUID,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = todo_service.update_todo(db, todo_id, todo, current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


# 🔹 DELETE
@router.delete("/{todo_id}")
def delete_todo(
    todo_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = todo_service.delete_todo(db, todo_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}