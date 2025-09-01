from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

class Deposito(Base):
    __tablename__ = "depositos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    ubicacion: Mapped[str] = mapped_column(String(100), unique=True)
    
    def __repr__(self) -> str:
        return f"Deposito(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}')"
    
    # Falta movimientos_origen
    # Falta movimientos_destino
