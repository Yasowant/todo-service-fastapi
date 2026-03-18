from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from app.services import todo_service
from app.utils.dependencies import get_current_user
from app.models.user_model import User  # ✅ IMPORTANT

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# ✅ CREATE TODO
@router.post("/")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ FIX
):
    return todo_service.create_todo(db, todo, current_user.id)  # ✅ FIX


# ✅ GET ALL TODOS
@router.get("/")
def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ FIX
):
    return todo_service.get_all_todos(db, current_user.id)  # ✅ FIX


# ✅ UPDATE TODO
@router.put("/{todo_id}")
def update_todo(
    todo_id: str,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ FIX
):
    updated = todo_service.update_todo(
        db,
        todo_id,
        todo.completed,
        current_user.id  # ✅ FIX
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated


# ✅ DELETE TODO
@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ FIX
):
    deleted = todo_service.delete_todo(
        db,
        todo_id,
        current_user.id  # ✅ FIX
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}