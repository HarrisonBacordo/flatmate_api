from datetime import datetime
from sqlmodel import SQLModel
from app.models.user import User


AuditBase = SQLModel(table=False)


class AuditCreate(AuditBase):
    created_by: User
    created_at: datetime
    updated_by: User
    updated_at: datetime

