from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    
    sku: Mapped[str] = mapped_column(String(100),
                                     unique=True,
                                     index=True)
    
    stock: Mapped[int] = mapped_column()

    stock_min: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
         return f"table: {self.__tablename__} 'id: {self.id},nombre: {self.nombre},sku: {self.sku},stock: {self.stock},stock_min: {self.stock_min}' "
    
    # movimientos: Mapped[ list[Movimiento] ] = mapped_column()