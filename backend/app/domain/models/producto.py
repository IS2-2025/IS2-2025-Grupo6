class Producto:
    id: int
    nombre: str
    sku: str
    stock: int
    stock_min: int

    def __init__(self,id: int,nombre: str,sku: str,stock: int,stock_min: int):
        self.id = id
        self.nombre = nombre
        self.sku = sku
        self.stock = stock
        self.stock_min = stock_min
    

    def __str__(self):
        return f"Producto(id: {self.id}, nombre: {self.nombre}, sku: {self.sku}, stock: {self.stock}, stock_min: {self.stock_min})"