from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from app.services import todo_service

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.post("/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)


@router.get("/")
def get_todos(db: Session = Depends(get_db)):
    return todo_service.get_all_todos(db)


@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated = todo_service.update_todo(db, todo_id, todo.completed)

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_service.delete_todo(db, todo_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}