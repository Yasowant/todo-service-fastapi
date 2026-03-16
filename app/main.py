from fastapi import FastAPI
from sqlalchemy import text
from app.database.database import engine,Base
from app.routes.todo_routes import router as todo_router

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"database": "connected"}

app.include_router(todo_router)
@app.get("/")
def home():
    return {"message":"FastAPI running successfully"} 