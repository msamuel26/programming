from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from extensions.database import Base


# Create a SQLAlchemy model for the Order
class AccountModel(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String)
    balance = Column(Integer)
    customer_id = Column(Integer)
