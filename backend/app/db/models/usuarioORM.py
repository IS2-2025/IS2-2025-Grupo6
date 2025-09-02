from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base import Base

class UsuarioORM(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)

    rol = relationship("UsuarioRolORM", back_populates="usuario")
    movimientos = relationship("MovimientoORM", back_populates="usuario")

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, username='{self.username}', email='{self.email}', is_active={self.is_active})"