import uuid
from datetime import datetime
from fastapi import APIRouter
from app.core.deps import SessionDep, CurrentUser
from app.models.calendar_event import CalendarEvent, CalendarEventCreate, CalendarEventRead


router = APIRouter(prefix="/calendar-events", tags=["calendar-events"])


@router.get("/{event_id}", response_model=CalendarEventRead)
def get_calendar_event(event_id: uuid.UUID, session: SessionDep):
    return session.get(CalendarEvent, event_id)


@router.put("/{event_id}", response_model=CalendarEventRead)
def update_calendar_event(
    event_id: uuid.UUID,
    event_update: CalendarEventCreate,
    session: SessionDep,
    current_user: CurrentUser,
):
    event = session.get(CalendarEvent, event_id)
    if event:
        event.title = event_update.title
        event.description = event_update.description
        event.event_date = event_update.event_date
        event.updated_by = current_user.id
        event.updated_at = datetime.utcnow()
        session.add(event)
        session.commit()
        session.refresh(event)
    return event


@router.post("/", response_model=CalendarEventRead)
def create_calendar_event(
    event_create: CalendarEventCreate, session: SessionDep, current_user: CurrentUser
):
    event = CalendarEvent(
        title=event_create.title,
        description=event_create.description,
        event_date=event_create.event_date,
        flat_id=event_create.flat_id,
        created_by=current_user.id,
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    return event
