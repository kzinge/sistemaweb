from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database.database import Base

class User(Base, UserMixin):
    __tablename__ = 'users'
    
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash : Mapped[str] = mapped_column(String, nullable=False)
    
    def get_id(self):
        return self.id

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username})"

    def __init__(self,username, password_hash):
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def all_users(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_username(cls, session, username):
        return session.query(cls).filter_by(username=username).first()
    
    @classmethod
    def create_user(cls, session, username, password_hash):
        new_user = cls(id=None, username=username, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        return new_user
    
    def delete_user(self, session, user):
        session.delete(user)
        session.commit()
    