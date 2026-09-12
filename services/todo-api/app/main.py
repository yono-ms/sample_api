from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from .routers import auth, todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Todo API for Android",
    description="Backend REST API for Android Todo Application with user authentication and SQLite persistence.",
    version="1.0.0",
    lifespan=lifespan,
)

# Enable CORS for Android emulator (10.0.2.2), physical devices, and web frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(todos.router)


@app.get("/")
def root():
    return {
        "message": "Todo API Service is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "todo-api"}
