from fastapi import FastAPI, HTTPException
from app.routers import todo
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = [
#     "http://127.0.0.1:5501",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

app.include_router(todo.router, tags=["Todo"])
