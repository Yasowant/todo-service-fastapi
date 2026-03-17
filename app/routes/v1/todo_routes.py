from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from app.services import todo_service
from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# ✅ CREATE TODO (Protected)
@router.post("/")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    return todo_service.create_todo(db, todo, user_id)


# ✅ GET ALL TODOS (User-specific)
@router.get("/")
def get_todos(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    return todo_service.get_all_todos(db, user_id)


# ✅ UPDATE TODO (Protected + Ownership check)
@router.put("/{todo_id}")
def update_todo(
    todo_id: str,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    updated = todo_service.update_todo(
        db, todo_id, todo.completed, user_id
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated


# ✅ DELETE TODO (Protected + Ownership check)
@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    deleted = todo_service.delete_todo(db, todo_id, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}