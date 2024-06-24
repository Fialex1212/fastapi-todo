from sqlalchemy.orm import Session
from app.models.todo import Todo as DBTodo
from app.schemas.todo import TodoCreate, TodoUpdate


def create_todo(db: Session, todo: TodoCreate):
    db_todo = DBTodo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, todo_id: int):
    return db.query(DBTodo).filter(DBTodo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 30):
    return db.query(DBTodo).offset(skip).limit(limit).all()

def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
    db_todo = db.query(DBTodo).filter(DBTodo.id == todo_id).first()
    if db_todo:
        db_todo.title = todo_update.title
        db_todo.content = todo_update.content
        db_todo.active = todo_update.active
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(DBTodo).filter(DBTodo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo