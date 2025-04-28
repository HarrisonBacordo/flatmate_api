import uuid
from argon2 import PasswordHasher
from sqlmodel import select
from app.core.deps import SessionDep
from app.models.user import User, UserCreate


# CRUD operations for User model
def create_user(session: SessionDep, user: UserCreate) -> User:
    db_obj = User.model_validate(
        user, update={"hashed_password": PasswordHasher().hash(user.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(session: SessionDep, email: str) -> User | None:
    return session.exec(select(User).where(User.email == email)).first()


def get_user_by_id(session: SessionDep, id: uuid.UUID) -> User | None:
    return session.get(User, id)


def authenticate_user(session: SessionDep, email: str, password: str) -> User | None:
    user = get_user_by_email(session, email)
    if not user:
        return False
    if not PasswordHasher().verify(user.hashed_password, password):
        return False
    return user
