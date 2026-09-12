import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////app/data/todo.db")

# In local dev outside docker, fall back to relative path if /app/data doesn't exist
if DATABASE_URL.startswith("sqlite:////app/data") and not os.path.exists("/app/data"):
    os.makedirs("./data", exist_ok=True)
    DATABASE_URL = "sqlite:///./data/todo.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
