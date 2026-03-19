import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    priority=Column(String,default="medium")
    category=Column(String,default="personal")
    due_date=Column(String,nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))