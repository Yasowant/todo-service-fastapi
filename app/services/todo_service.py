from sqlalchemy.orm import Session
from app.models.todo_model import Todo


# ✅ CREATE TODO
def create_todo(db: Session, todo, user_id: int):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False,
        user_id=user_id   # 🔐 link to user
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# ✅ GET ALL TODOS (ONLY USER'S TODOS)
def get_all_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


# ✅ UPDATE TODO (ONLY IF OWNER)
def update_todo(db: Session, todo_id: int, completed: bool, user_id: int):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id   # 🔐 ownership check
    ).first()

    if not todo:
        return None

    todo.completed = completed
    db.commit()
    db.refresh(todo)

    return todo


# ✅ DELETE TODO (ONLY IF OWNER)
def delete_todo(db: Session, todo_id: int, user_id: int):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id   # 🔐 ownership check
    ).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return True