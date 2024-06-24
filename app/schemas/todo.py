from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    content: Optional[str] = None
    active: bool

class TodoCreate(TodoBase):
    author_id: id

class TodoUpdate(TodoBase):
    pass 

class Todo(TodoBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True