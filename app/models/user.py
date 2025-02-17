from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class CreateUserResponse(BaseModel):
    message: str
    created_at: str
    username: str


class CurrentUserResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    created_at: str

