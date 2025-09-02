from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String
from app.db.base import Base
from .movimientoORM import MovimientoORM

class DepositoORM(Base):
    __tablename__ = "depositos"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    ubicacion: Mapped[str] = mapped_column(String(100), unique=True)
    
    def __repr__(self) -> str:
        return f"Deposito(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}')"
    
    movimientos_origen = relationship("MovimientoORM",foreign_keys=[MovimientoORM.deposito_origen_id],back_populates="deposito_origen")
    movimientos_destino = relationship("MovimientoORM",foreign_keys=[MovimientoORM.deposito_destino_id],back_populates="deposito_destino")