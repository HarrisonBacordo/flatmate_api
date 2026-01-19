import uuid
from sqlmodel import SQLModel, Field


class FlatBase(SQLModel):
    name: str = Field(nullable=False)
    address: str | None = Field(default=None)


class Flat(FlatBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class FlatCreate(FlatBase):
    pass


class FlatRead(FlatBase):
    id: uuid.UUID