# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from src.db.crud import create_item, read_item
# from src.db.database import SessionLocal, Item

# router = APIRouter()

# @router.post("/items/")
# def create_item_route(item: Item, db: Session = Depends(SessionLocal)):
#     return create_item(db=db, item=item)

# @router.get("/items/{item_id}")
# def read_item_route(item_id: int, db: Session = Depends(SessionLocal)):
#     item = read_item(db=db, item_id=item_id)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item