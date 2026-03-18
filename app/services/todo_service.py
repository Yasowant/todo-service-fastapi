from uuid import UUID
from sqlalchemy.orm import Session
from app.models.todo_model import Todo


# CREATE
def create_todo(db: Session, todo, user_id: UUID):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False,
        user_id=user_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# GET
def get_all_todos(db: Session, user_id: UUID):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


# UPDATE
def update_todo(db: Session, todo_id: UUID, completed: bool, user_id: UUID):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()

    if not todo:
        return None

    todo.completed = completed
    db.commit()
    db.refresh(todo)

    return todo


# DELETE
def delete_todo(db: Session, todo_id: UUID, user_id: UUID):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return True