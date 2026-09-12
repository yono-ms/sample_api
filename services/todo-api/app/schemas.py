from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


# --- Auth & User Schemas ---

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username for login")
    password: str = Field(..., min_length=6, max_length=100, description="Password (at least 6 characters)")


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: Optional[str] = None


# --- Todo Schemas ---

class TodoCreate(BaseModel):
    memo: str = Field(..., min_length=1, description="Content of the memo/todo")
    due_date: Optional[datetime] = Field(None, description="Due date and time (ISO 8601, optional)")


class TodoUpdate(BaseModel):
    memo: Optional[str] = Field(None, min_length=1, description="Content of the memo/todo")
    due_date: Optional[datetime] = Field(None, description="Due date and time")
    is_completed: Optional[bool] = Field(None, description="Completion status")


class TodoResponse(BaseModel):
    id: int
    memo: str
    created_at: datetime
    due_date: Optional[datetime] = None
    is_completed: bool
    user_id: int

    model_config = ConfigDict(from_attributes=True)
