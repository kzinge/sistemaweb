from sqlalchemy import ForeignKey, String, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .user import User
from ..database.config import Base

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
