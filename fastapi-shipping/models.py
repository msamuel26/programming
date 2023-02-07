# models.py berisi definisi tabel dan Pydantic, serta standard CRUD

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base
from pydantic import BaseModel, Field

# Create a Pydantic model for the Shipping
class ShippingCreate(BaseModel):
    status: str = Field(..., example='Delivered')
    customer_id: int = Field(..., example=4)

# Create a SQLAlchemy model for the Shipping
class Shipping(Base):
    __tablename__ = 'shippings'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    customer_id = Column(Integer)

def create_shipping(db: Session, status: str, customer_id: int):
    shipping = Shipping(status=status, customer_id=customer_id)
    print(shipping)
    db.add(shipping)
    db.commit()
    db.refresh(shipping)
    return shipping

def get_shipping(db: Session, shipping_id: int):
    return db.query(Shipping).filter(Shipping.id == shipping_id).first()

def update_shipping(db: Session, shipping_id: int, status: str, customer_id: int):
    shipping = get_shipping(db, shipping_id)
    shipping.status = status
    shipping.customer_id = customer_id
    db.commit()
    db.refresh(shipping)
    return shipping

def get_shippings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Shipping).offset(skip).limit(limit).all()

def delete_shipping(db: Session, shipping_id: int):
    shipping = get_shipping(db, shipping_id)
    db.delete(shipping)
    db.commit()
