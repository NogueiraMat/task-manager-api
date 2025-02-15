from pydantic import BaseModel
from datetime import datetime


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class CreateUserResponse(BaseModel):
    message: str
    created_at: str
    username: str

