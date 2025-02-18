from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse

from utils.security import validate_session

from database.connection import get_db
from sqlalchemy.orm import Session

from models.task import CreateTaskRequest, CreateTaskResponse, GetTasksResponse

from schemas.task import Task
from schemas.user import User


router = APIRouter()


@router.post("/task")
def add_task(
    data: CreateTaskRequest,
    session=Depends(validate_session),
    db: Session = Depends(get_db),
):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    new_task = Task(
        title=data.title,
        description=data.description,
        user_id=user_id.id,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return JSONResponse(
        CreateTaskResponse(
            id=new_task.id,
            title=new_task.title,
            description=new_task.description,
            created_at=str(new_task.created_at),
            updated_at=str(new_task.updated_at),
        ).model_dump(),
        status_code=status.HTTP_201_CREATED,
    )


@router.get("/task")
def get_task(session=Depends(validate_session), db: Session = Depends(get_db)):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    tasks = db.query(Task).filter_by(user_id=user_id.id).all()

    return JSONResponse(
        [
            GetTasksResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                created_at=str(task.created_at),
                updated_at=str(task.updated_at),
                task_status=task.status,
            ).model_dump()
            for task in tasks
        ],
        status_code=status.HTTP_200_OK,
    )


@router.get("/task/{id}")
def get_task_by_id(
    id: int, session=Depends(validate_session), db: Session = Depends(get_db)
):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    task = db.query(Task).filter_by(user_id=user_id.id, id=id).first()

    if not task:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Tarefa não encontrada!",
            },
        )

    return JSONResponse(
        GetTasksResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            created_at=str(task.created_at),
            updated_at=str(task.updated_at),
            task_status=task.status,
        ).model_dump(),
        status_code=status.HTTP_200_OK,
    )


@router.delete("/task/{id}")
def delete_task(
    id: int, session=Depends(validate_session), db: Session = Depends(get_db)
):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    task = db.query(Task).filter_by(user_id=user_id.id, id=id).first()

    if not task:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Tarefa não encontrada!",
            },
        )

    db.delete(task)
    db.commit()

    return JSONResponse(
        {
            "message": "Tarefa deletada com sucesso!",
        },
        status_code=status.HTTP_200_OK,
    )


@router.put("/task/{id}")
def update_task(
    id: int,
    data: CreateTaskRequest,
    session=Depends(validate_session),
    db: Session = Depends(get_db),
):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    task = db.query(Task).filter_by(user_id=user_id.id, id=id).first()

    if not task:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Tarefa não encontrada!",
            },
        )

    task.title = data.title
    task.description = data.description

    db.commit()

    return JSONResponse(
        {
            "message": "Tarefa atualizada com sucesso!",
        },
        status_code=status.HTTP_200_OK,
    )


@router.patch("/task/finish/{id}")
def update_task_status(
    id: int, session=Depends(validate_session), db: Session = Depends(get_db)
):
    if not session:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Usuário não autenticado!",
            },
        )

    user_id = db.query(User).filter_by(username=session["sub"]).first()

    task = db.query(Task).filter_by(user_id=user_id.id, id=id).first()

    if not task:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Tarefa não encontrada!",
            },
        )

    task_status = task.status
    if task_status == 1:
        return HTTPException(
            status_code=status.HTTP_200_OK,
            detail={
                "message": "Tarefa já finalizada!",
            },
        )

    task.status = 1

    db.commit()

    return JSONResponse(
        {
            "message": "Tarefa atualizada com sucesso!",
        },
        status_code=status.HTTP_200_OK,
    )

