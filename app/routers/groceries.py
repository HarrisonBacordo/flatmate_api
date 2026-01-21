import uuid
from datetime import datetime
from fastapi import APIRouter
from app.core.deps import SessionDep, CurrentUser
from app.models.grocery import Grocery, GroceryCreate, GroceryRead


router = APIRouter(prefix="/groceries", tags=["groceries"])


@router.get("/{grocery_id}", response_model=GroceryRead)
def get_grocery(grocery_id: uuid.UUID, session: SessionDep):
    return session.get(Grocery, grocery_id)


@router.put("/{grocery_id}", response_model=GroceryRead)
def update_grocery(
    grocery_id: uuid.UUID,
    grocery_update: GroceryCreate,
    session: SessionDep,
    current_user: CurrentUser,
):
    grocery = session.get(Grocery, grocery_id)
    if grocery:
        grocery.name = grocery_update.name
        grocery.quantity = grocery_update.quantity
        grocery.purchased = grocery_update.purchased
        grocery.updated_by = current_user.id
        grocery.updated_at = datetime.utcnow()
        session.add(grocery)
        session.commit()
        session.refresh(grocery)
    return grocery


@router.post("/", response_model=GroceryRead)
def create_grocery(
    grocery_create: GroceryCreate, session: SessionDep, current_user: CurrentUser
):
    grocery = Grocery(
        name=grocery_create.name,
        quantity=grocery_create.quantity,
        purchased=grocery_create.purchased,
        flat_id=grocery_create.flat_id,
        created_by=current_user.id,
    )
    session.add(grocery)
    session.commit()
    session.refresh(grocery)
    return grocery

