from tienda import Tienda
from cliente import Cliente
from producto import Producto

class TiendaService:
    def __init__(self):
        self.tienda = Tienda("Tienda Online Carlos")

    def cargar_productos_demo(self):
        productos_demo = [
            Producto("Laptop", 1200, 3),
            Producto("Mouse", 25, 40),
            Producto("Teclado", 45, 20),
        ]
        for producto in productos_demo:
            self.tienda.agregar_producto(producto)

    def comprar(self, cliente: Cliente, nombre_producto: str, cantidad: int):
        producto = self.tienda.buscar_producto(nombre_producto)
        if not producto:
            return f"El producto '{nombre_producto}' no existe."

        if producto.stock < cantidad:
            return "No hay suficiente stock."

        producto.actualizar_stock(-cantidad)
        return f"{cliente.nombre} compró {cantidad} unidad(es) de {producto.nombre}."

    def mostrar_productos(self):
        return "\n".join(self.tienda.listar_productos())
