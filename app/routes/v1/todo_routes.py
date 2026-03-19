from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoResponse
from app.services import todo_service
from app.utils.dependencies import get_current_user
from app.models.user_model import User

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


# 🔹 CREATE TODO
@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return todo_service.create_todo(db, todo, current_user.id)


# 🔹 GET ALL TODOS
@router.get("/", response_model=list[TodoResponse])
def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return todo_service.get_all_todos(db, current_user.id)


# 🔹 GET SINGLE TODO (🔥 recommended)
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


# 🔹 UPDATE TODO (🔥 FIXED)
@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: UUID,  # ✅ FIXED (was str)
    todo: TodoUpdate,  # ✅ FULL OBJECT (not just completed)
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = todo_service.update_todo(
        db,
        todo_id,
        todo,  # ✅ PASS FULL OBJECT
        current_user.id
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated


# 🔹 DELETE TODO
@router.delete("/{todo_id}")
def delete_todo(
    todo_id: UUID,  # ✅ FIXED
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = todo_service.delete_todo(
        db,
        todo_id,
        current_user.id
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}