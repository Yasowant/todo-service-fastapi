from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


# 🔹 CREATE
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    priority: Optional[str] = "medium"
    category: Optional[str] = "personal"
    due_date: Optional[datetime] = None


# 🔹 UPDATE
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    due_date: Optional[datetime] = None


# 🔹 RESPONSE
class TodoResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: str
    priority: str
    category: str
    due_date: Optional[datetime]

    class Config:
        from_attributes = True