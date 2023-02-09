from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base
from pydantic import BaseModel, Field

# Create a Pydantic model for the Order
class OrderCreate(BaseModel):
    item: str = Field(..., example='Monitor')
    amount: int = Field(..., example=12000)
    customer_id: int = Field(..., example=2)

# Create a SQLAlchemy model for the Order
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    amount = Column(Integer)
    customer_id = Column(Integer)

def create_order(db: Session, item: str, amount: int, customer_id: int):
    order = Order(item=item, amount=amount, customer_id=customer_id)
    print(order)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order(db: Session, order_id: int, item: str, amount: int, customer_id: int):
    order = get_order(db, order_id)
    order.item = item
    order.amount = amount
    order.customer_id = customer_id
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    db.delete(order)
    db.commit()