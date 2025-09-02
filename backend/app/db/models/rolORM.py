from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base import Base

class RolORM(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)

    usuarios = relationship("UsuarioRolORM",back_populates="rol")

    def __repr__(self) -> str:
        return f"Rol(id={self.id}, nombre='{self.nombre}')"