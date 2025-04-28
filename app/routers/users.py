import uuid
from fastapi import APIRouter
from app.core.deps import SessionDep
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}")
def get_user(user_id: uuid.UUID, session: SessionDep):
    return session.get(User, user_id)
