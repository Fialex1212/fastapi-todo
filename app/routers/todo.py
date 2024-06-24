from fastapi import APIRouter, HTTPException, Depends, Path, Query
from sqlalchemy.orm import Session
from app.dependency import get_db
from app.crud.todo import get_todo, get_todos, create_todo, update_todo, delete_todo
from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from typing import Annotated

router = APIRouter()

@router.post("/todo", response_model=Todo)
def create_todo_endpoint(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return create_todo(db=db, todo=todo)

@router.get("/todo/{todo_id}", response_model=Todo)
def get_todo_endpoint(
    todo_id: Annotated[int, Path(..., title="The ID of the todo to get")],
    db: Session = Depends(get_db)
):
    db_todo = get_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.get("/todos", response_model=list[Todo])
def get_todos_endpoint(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(le=1000)] = 30,
    db: Session = Depends(get_db)
):
    return get_todos(db=db, skip=skip, limit=limit)
    

@router.put("/todo/{todo_id}", response_model=Todo)
def update_todo_endpoint(
    todo_id: Annotated[int, 0],
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):
    return update_todo(db=db, todo_id=todo_id, todo_update=todo)

@router.delete("/todo/{todo_id}", response_model=Todo)
def delete_todo_endpoint(
    todo_id: Annotated[int, 0],
    db: Session = Depends(get_db)
):
    return delete_todo(db=db, todo_id=todo_id)