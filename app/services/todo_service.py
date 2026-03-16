from sqlalchemy.orm import Session
from app.models.todo_model import Todo


def create_todo(db: Session, todo):
    new_todo = Todo(
        title=todo.title,
        description=todo.description
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todos(db: Session):
    return db.query(Todo).all()


def update_todo(db: Session, todo_id: int, completed: bool):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        return None

    todo.completed = completed
    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo