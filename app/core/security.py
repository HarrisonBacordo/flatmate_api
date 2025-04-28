from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings


def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    to_encode = {"exp": datetime.now(timezone.utc) + expires_delta, "sub": str(subject)}
    print(settings.SECRET_KEY)
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
