from app.db.models.productoORM import ProductoORM
from app.domain.models.producto import Producto

class ProductoMapper:
    def orm_to_domain(orm: ProductoORM) -> Producto:
        return Producto(orm.id,orm.nombre,orm.sku,orm.stock,orm.stock_min)
    
    def domain_to_orm(domain: Producto) -> ProductoORM:
        return ProductoORM(
            id= domain.id,
            nombre= domain.nombre,
            sku= domain.sku,
            stock= domain.stock,
            stock_min= domain.stock_min      
        )