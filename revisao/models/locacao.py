from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String,Date, ForeignKey

class Locacao(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[Date] = mapped_column(Date, nullable=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey('cliente.id'))
    veiculo_id: Mapped[int] = mapped_column(ForeignKey('veiculo.id'))

    cliente: Mapped['Cliente'] = relationship('Cliente', back_populates='locacoes')
    veiculo: Mapped['Veiculo'] = relationship('Veiculo', back_populates='locacoes')