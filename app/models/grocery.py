import uuid
from datetime import datetime
from sqlmodel import Field, SQLModel


class GroceryBase(SQLModel):
    name: str = Field(max_length=100, nullable=False)
    quantity: int = Field(default=1, nullable=False)
    purchased: bool = Field(default=False, nullable=False)


class Grocery(GroceryBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    flat_id: uuid.UUID = Field(foreign_key="flat.id", nullable=False)
    created_by: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_by: uuid.UUID | None = Field(foreign_key="user.id", default=None)
    updated_at: datetime | None = Field(default=None)


class GroceryCreate(GroceryBase):
    flat_id: uuid.UUID


class GroceryRead(GroceryBase):
    id: uuid.UUID
    flat_id: uuid.UUID
    created_by: uuid.UUID
    created_at: datetime
    updated_by: uuid.UUID | None
    updated_at: datetime | None
