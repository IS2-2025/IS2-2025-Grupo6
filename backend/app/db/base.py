from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .models.depositoORM import DepositoORM
from .models.movimientoORM import MovimientoORM
from .models.productoORM import ProductoORM
from .models.rolORM import RolORM
from .models.usuarioORM import UsuarioORM
from .models.usuarioRolORM import UsuarioRolORM