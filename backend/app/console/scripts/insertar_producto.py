from app.db.session import sessionLocal
from app.db.models.productoORM import ProductoORM

def insertar_producto_de_ejemplo():
  
    with sessionLocal() as session:
        try:
            nuevo_producto = ProductoORM(
                nombre="Mouse Gamer",
                sku="MGA-001",
                stock=50,
                stock_min=10
            )

            session.add(nuevo_producto)
            session.commit()

            # Refrescamos el objeto para obtener el ID asignado por la base de datos.
            # Sin esta línea, nuevo_producto.id no tendría el valor correcto.
            session.refresh(nuevo_producto)
            
            print("------------------------------------------")
            print(f"✅ Producto insertado con exito con ID: {nuevo_producto.id}")
            print(f"Nombre: {nuevo_producto.nombre}")
            print(f"SKU: {nuevo_producto.sku}")
            print("------------------------------------------")

        except Exception as e:
            # En caso de error, hacemos un rollback para no dejar la base de datos en un estado inconsistente.
            session.rollback()
            print("------------------------------------------")
            print("❌ Ocurrió un error al insertar el producto.")
            print(f"Detalles del error: {e}")
            print("------------------------------------------")


if __name__ == "__main__":
    insertar_producto_de_ejemplo()
