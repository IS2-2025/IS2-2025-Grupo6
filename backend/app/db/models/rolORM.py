from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from app.db.base import Base

class Rol(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    
    usuarios: Mapped[list["UsuarioRol"]] = relationship(back_populates="rol")

    def __repr__(self) -> str:
        return f"Rol(id={self.id}, nombre='{self.nombre}')"
    
    # Falta usuarios
