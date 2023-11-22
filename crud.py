from sqlalchemy.orm import Session
from .database import Item

def create_item(db: Session, item: Item):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()