from tienda_service import TiendaService
from cliente import Cliente

def main():
    service = TiendaService()
    service.cargar_productos_demo()

    print("=== PRODUCTOS DISPONIBLES ===")
    print(service.mostrar_productos())

    cliente = Cliente("Carlos", "carlos@example.com")

    print("\n=== COMPRA ===")
    resultado = service.comprar(cliente, "Laptop", 1)
    print(resultado)

    print("\n=== PRODUCTOS TRAS COMPRA ===")
    print(service.mostrar_productos())

if __name__ == "__main__":
    main()
