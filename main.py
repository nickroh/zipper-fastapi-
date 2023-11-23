from fastapi import FastAPI
from .routers import items, users

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html = True), name="static")

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])