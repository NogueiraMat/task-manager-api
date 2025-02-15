from datetime import timedelta, datetime
from dotenv import load_dotenv
from jwt import InvalidTokenError, ExpiredSignatureError
import bcrypt
import jwt
import os


load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_jwt_token(data: dict, expire: timedelta = None):
    encoded_data = data.copy()

    expires = (
        datetime.now() + expire if expire else datetime.now() + timedelta(minutes=30)
    )
    encoded_data["exp"] = expires

    token = jwt.encode(encoded_data, SECRET_KEY, algorithm=ALGORITHM)

    return token, expires


def validate_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        return False
    except InvalidTokenError:
        return False


def create_hashed_string(text: str) -> str:
    salt = bcrypt.gensalt()
    hashed_string = bcrypt.hashpw(text.encode("utf-8"), salt=salt)
    return hashed_string.decode("utf-8")


def validate_hashed_string(text: str, hashed_text: str) -> bool:
    return bcrypt.checkpw(text.encode("utf-8"), hashed_text.encode("utf-8"))

