from uuid import UUID
from sqlalchemy.orm import Session
from app.models.todo_model import Todo


# 🔹 CREATE
def create_todo(db: Session, todo, user_id: UUID):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False,
        priority=todo.priority,
        category=todo.category,
        due_date=todo.due_date,
        user_id=user_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# 🔹 GET ALL
def get_all_todos(db: Session, user_id: UUID):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


# 🔹 GET SINGLE (Optional but useful)
def get_todo(db: Session, todo_id: UUID, user_id: UUID):
    return db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()


# 🔹 UPDATE (🔥 FULL FLEXIBLE UPDATE)
def update_todo(db: Session, todo_id: UUID, todo_data, user_id: UUID):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()

    if not todo:
        return None

    # ✅ Only update fields that are provided
    if todo_data.title is not None:
        todo.title = todo_data.title

    if todo_data.description is not None:
        todo.description = todo_data.description

    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    if todo_data.priority is not None:
        todo.priority = todo_data.priority

    if todo_data.category is not None:
        todo.category = todo_data.category

    if todo_data.due_date is not None:
        todo.due_date = todo_data.due_date

    db.commit()
    db.refresh(todo)

    return todo


# 🔹 DELETE
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