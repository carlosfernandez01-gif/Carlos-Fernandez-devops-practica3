class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad: int):
        if self.stock + cantidad < 0:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock += cantidad

    def __str__(self):
        return f"{self.nombre} - {self.precio}€ - Stock: {self.stock}"
