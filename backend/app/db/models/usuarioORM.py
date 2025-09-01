from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, username='{self.username}', email='{self.email}', is_active={self.is_active})"
    
    # Falta roles
    # Falta movimientos
