from sqlalchemy import Table, ForeignKey, Column, String, Date, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.config import Base
from flask_login import UserMixin


class User(UserMixin, Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column(String(150), nullable= False)

    noticias: Mapped[list['Noticia']] = relationship("Noticia", back_populates="usuario", cascade="all, delete-orphan")

    def get_id(self):
        return self.id
    
    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nome='{self.nome}', email={self.email})"
    
    def __init__(self, nome,email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

class Noticia(Base):
    __tablename__ = 'noticias'

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable = False)
    data: Mapped[str] = mapped_column(Date, nullable = False)
    descricao: Mapped[str] = mapped_column(Text, nullable= False)
    user_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable= False)

    usuario: Mapped['User'] = relationship('User', back_populates='noticias')

    def __repr__(self) -> str:
        return f"Noticia (id={self.id}, nome='{self.titulo}', email={self.data})"
    
    def __init__(self, nome,data, descricao, user_id) -> None:
        self.titulo = nome
        self.data = data
        self.descricao = descricao
        self.user_id = user_id
