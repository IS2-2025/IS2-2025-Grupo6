from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id: Mapped[int] = mapped_column(primary_key=True,index=True, autoincrement=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"))
    deposito_origen_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"))
    deposito_destino_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    cantidad: Mapped[int] = mapped_column()
    fecha: Mapped[datetime] = mapped_column()
    tipo: Mapped[int] = mapped_column()

    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id], back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id], back_populates="movimientos_destino")
    producto = relationship("ProductoORM", back_populates="movimientos")
    usuario = relationship("UsuarioORM", back_populates="movimientos")