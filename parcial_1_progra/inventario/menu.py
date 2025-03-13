from inventario import Tienda
from inventario import Cliente
from inventario import Producto

def menu():
    tienda = Tienda()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Agregar cliente")
        print("3. Realizar venta")
        print("4. Mostrar productos")
        print("5. Mostrar clientes")
        print("6. Guardar datos")
        print("7. Cargar datos")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            id = int(input("ID del producto: "))
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            producto = Producto(nombre, id, precio, cantidad)
            tienda.agregar_producto(producto)
        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            id = int(input("ID del cliente: "))
            saldo = float(input("Saldo del cliente: "))
            cliente = Cliente(nombre, id, saldo)
            tienda.agregar_cliente(cliente)
        elif opcion == "3":
            id_cliente = int(input("ID del cliente: "))
            id_producto = int(input("ID del producto: "))
            cantidad = int(input("Cantidad a comprar: "))
            tienda.realizar_venta(id_cliente, id_producto, cantidad)
        elif opcion == "4":
            tienda.mostrar_productos()
        elif opcion == "5":
            tienda.mostrar_clientes()
        elif opcion == "6":
            archivo = input("Nombre del archivo para guardar los datos: ")
            tienda.guardar_datos(archivo)
        elif opcion == "7":
            archivo = input("Nombre del archivo para cargar los datos: ")
            tienda.cargar_datos(archivo)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()