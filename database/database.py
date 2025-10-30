from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///banco.db")
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass