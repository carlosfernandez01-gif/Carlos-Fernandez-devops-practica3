from producto import Producto

class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def listar_productos(self):
        return [str(p) for p in self.productos]
