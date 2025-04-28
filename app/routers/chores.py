import uuid
from fastapi import APIRouter, Depends
from app.dependencies import SessionDep
from app.models.chore import Chore


router = APIRouter(prefix="/chores", tags=["chores"])


@router.get("/{chore_id}")
def get_chore(chore_id: uuid.UUID, session: SessionDep):
    return session.get(Chore, chore_id)


@router.put("/{chore_id}")
def update_chore(chore_id: uuid.UUID, chore: Chore, session: SessionDep):
    session.add(chore)
    session.commit()
    session.refresh(chore)
    return chore


@router.post("/")
def create_chore(chore: Chore, session: SessionDep):
    session.add(chore)
    session.commit()
    session.refresh(chore)
    return chore
