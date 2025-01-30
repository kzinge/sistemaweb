from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class Veiculo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=True)

    # Relacionamento com Locacao
    locacoes: Mapped[list["Locacao"]] = relationship('Locacao', back_populates='veiculo')