from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database.config import Base
from flask_login import UserMixin

class User(UserMixin, Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column(String(150), nullable= False)

    noticias = relationship("Noticia", back_populates="usuario", cascade="all, delete-orphan")

    def get_id(self):
        return self.id
    
    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nome='{self.nome}', email={self.email})"
    
    def __init__(self, nome,email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha