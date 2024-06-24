from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Todo(Base):
    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    active = Column(Boolean)

    author = relationship("User", back_populates="todos")
    author_id = Column(Integer, ForeignKey("users.id"))