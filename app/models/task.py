from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    description: str


class CreateTaskResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: str
    updated_at: str


class GetTasksResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: str
    updated_at: str
    task_status: bool

