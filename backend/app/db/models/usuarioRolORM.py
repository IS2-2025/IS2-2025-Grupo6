from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.db.base import Base

class UsuarioRolORM(Base):
    __tablename__ = "usuario_rol"

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"),primary_key=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey("roles.id"),primary_key=True)

    usuario = relationship("UsuarioORM", back_populates="roles")
    rol = relationship("RolORM", back_populates="usuarios")

    def __repr__(self) -> str:
        return f"UsuarioRol(usuario_id={self.usuario_id}, rol_id={self.rol_id})"