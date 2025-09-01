from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer
from app.db.base import Base
from .usuario import Usuario
from .rol import Rol

class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        primary_key=True
    )
    rol_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        primary_key=True
    )

    usuario: Mapped[Usuario] = relationship("Usuario", back_populates="roles")
    rol: Mapped[Rol] = relationship("Rol", back_populates="usuarios")

    def __repr__(self) -> str:
        return f"UsuarioRol(usuario_id={self.usuario_id}, rol_id={self.rol_id})"    
    
# Relaciones bidireccionales (relationship con back_populates y foreign_keys). Esto permite navegar fácilmente entre las clases, por ejemplo, puedes acceder al producto relacionado con un movimiento usando movimiento.producto.    
