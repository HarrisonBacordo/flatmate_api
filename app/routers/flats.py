import uuid
from fastapi import APIRouter, Depends
from app.core.deps import SessionDep
from app.models.flat import Flat


router = APIRouter(prefix="/flats", tags=["flats"])


@router.get("/{flat_id}")
def get_flat(flat_id: uuid.UUID, session: SessionDep):
    return session.get(Flat, flat_id)


@router.put("/{flat_id}")
def update_flat(flat_id: uuid.UUID, flat: Flat, session: SessionDep):
    session.add(flat)
    session.commit()
    session.refresh(flat)
    return flat


@router.post("/")
def create_flat(flat: Flat, session: SessionDep):
    session.add(flat)
    session.commit()
    session.refresh(flat)
    return flat
