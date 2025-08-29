from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    
    sku: Mapped[str] = mapped_column(String(100),
                                     unique=True,
                                     index=True)
    
    stock: Mapped[int] = mapped_column()

    # movimientos: Mapped[ list[Movimiento] ] = mapped_column()