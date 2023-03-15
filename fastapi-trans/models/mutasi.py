from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session
from extensions.database import Base

class Mutation(Base):
    __tablename__ = 'mutasi'
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer)
    amount_trans = Column(Integer)
    balance = Column(Integer)