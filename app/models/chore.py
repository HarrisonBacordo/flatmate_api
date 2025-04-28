from sqlmodel import Field, SQLModel
import uuid


class Chore(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=100, nullable=False)
    description: str | None = Field(max_length=255, nullable=True)
    completed: bool = Field(default=False, nullable=False)
    assignee_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    flat_id: uuid.UUID = Field(foreign_key="flat.id", nullable=False)
    created_by: uuid.UUID = Field(foreign_key="user.id", nullable=False)
