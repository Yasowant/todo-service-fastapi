from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    completed: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True