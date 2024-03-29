from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO split db credentials into env variables
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/moses_trans"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()