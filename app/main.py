from fastapi import FastAPI
from app.routers import todo
from app.database import Base, engine
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

allowed_origins = [origin.strip() for origin in allowed_origins if origin.strip()]

if not allowed_origins:
    raise HTTPException(status_code=500, detail="No allowed origins configured")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(todo.router, tags=["Todo"])
