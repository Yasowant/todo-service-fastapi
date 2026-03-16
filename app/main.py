from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine,Base
from app.routes.todo_routes import router as todo_router

Base.metadata.create_all(bind=engine)

app=FastAPI()


origins = [
    "http://localhost:8080",   # React / Next dev server
    "http://127.0.0.1:8080",   # Local alternative
    "https://radiant-list-studio.vercel.app"  # Your deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"database": "connected"}

app.include_router(todo_router)
@app.get("/")
def home():
    return {"message":"FastAPI running successfully"} 