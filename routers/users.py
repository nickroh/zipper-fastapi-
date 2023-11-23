from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import create_user, read_user
from ..database import SessionLocal, User

router = APIRouter()

@router.post("/users/")
def create_user_route(user: User, db: Session = Depends(SessionLocal)):
    return create_user(db=db, user=user)

@router.get("/users/{user_id}")
def read_user_route(user_id: int, db: Session = Depends(SessionLocal)):
    user = read_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user