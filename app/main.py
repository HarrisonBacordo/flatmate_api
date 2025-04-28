from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import auth, chores, users
from app.db import create_db_and_tables, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(chores.router)
