from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session
from extensions.database import Base

# Create a SQLAlchemy model for the Shipping
class ShippingModel(Base):
    __tablename__ = "shippings"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    customer = Column(Integer)