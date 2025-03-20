from datetime import timedelta

from fastapi import APIRouter, Response, status, HTTPException, Depends
from fastapi.responses import JSONResponse

from database.connection import get_db
from sqlalchemy.orm import Session

from utils.security import create_jwt_token, validate_hashed_string
from models.auth import AuthRequest, AuthResponse
from schemas.user import User


router = APIRouter()


@router.post("/authentication")
def authentication(
    response: Response, data: AuthRequest, db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter_by(username=data.username).scalar()
    if not existing_user:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não cadastrado!"
        )

    validate_password = validate_hashed_string(data.password, existing_user.password)
    if not validate_password:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha incorreta!"
        )

    to_encode_data = {"sub": existing_user.username}

    access_token, expires_access_token = create_jwt_token(
        data=to_encode_data, expire=timedelta(minutes=30)
    )

    refresh_token, expires_refresh_token = create_jwt_token(
        data=to_encode_data, expire=timedelta(days=30)
    )

    response = JSONResponse(
        AuthResponse(
            username=existing_user.username,
            first_name=existing_user.first_name,
            last_name=existing_user.last_name,
            access_token=access_token,
        ).model_dump(),
        status_code=status.HTTP_200_OK,
    )

    response.set_cookie(
        "access_token",
        f"{access_token}",
        expires=expires_access_token.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    )
    response.set_cookie(
        "refresh_token",
        f"{refresh_token}",
        expires=expires_refresh_token.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    )

    return response


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return JSONResponse({"message": "Logout realizado com sucesso!"})
