from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session
from extensions.database import Base

# Create a SQLAlchemy model for the Order
class OrderModel(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    amount = Column(Integer)
    customer_id = Column(Integer)