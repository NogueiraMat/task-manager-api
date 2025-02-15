from datetime import datetime

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from database.connection import get_db
from sqlalchemy.orm import Session

from models.user import CreateUserRequest, CreateUserResponse
from utils.security import create_hashed_string
from schemas.user import User


router = APIRouter()


@router.post("/user")
def add_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(username=data.username).first()
    if existing_user:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Erro ao criar o usuário!",
            },
        )
    hashed_password = create_hashed_string(data.password)

    new_user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        username=data.username,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse(
        CreateUserResponse(
            message="Usuário criado com sucesso!",
            created_at=str(datetime.now()),
            username=data.username,
        ).model_dump(),
        status_code=status.HTTP_201_CREATED,
    )

