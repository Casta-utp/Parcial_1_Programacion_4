class Producto:

    def __init__ (self, nombre, id, precio, cantidad):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidad = cantidad #La cantidad se da en unidades (inventario)

    def __str__ (self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
    def disminuir_inventario(self, cantidad: int):
        print(f"Disminuyendo {cantidad} unidades de {self.nombre}")
        self.cantidad -= cantidad
    
    def aumentar_inventario(self, cantidad: int):
        print(f"Aumentando {cantidad} unidades de {self.nombre}")
        self.cantidad += cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad}")

class Cliente:

    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Saldo: {self.saldo}"
    
    def realizar_compra(self, producto: Producto, cantidad: int):
        if producto.cantidad >= cantidad and self.saldo >= producto.precio * cantidad:
            print(f"Realizando compra de {cantidad} unidades de {producto.nombre}")
            producto.disminuir_inventario(cantidad)
            self.saldo -= producto.precio * cantidad
        elif self.saldo < producto.precio * cantidad:
            print("Saldo insuficiente")
        else:
            print(f"No hay suficientes unidades de {producto.nombre}")
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}, Saldo: {self.saldo}")

class Tienda:

    lista_productos_disponibles = []
    lista_clientes_registrados = []

    def agregar_producto(self, producto: Producto):
        self.lista_productos_disponibles.append(producto)

    def agregar_cliente(self, cliente: Cliente):
        self.lista_clientes_registrados.append(cliente)

    def realizar_venta(self, id_cliente: int, id_producto: int, cantidad: int):
        cliente = None
        producto = None
        for c in self.lista_clientes_registrados: #recorro la lista de clientes e identifico el cliente con el id
            if c.id == id_cliente:
                cliente = c
                break
        for p in self.lista_productos_disponibles: #recorro la lista de productos e identifico el producto con el id
            if p.id == id_producto:
                producto = p
                break
        if cliente != None and producto != None: #si el cliente y el producto existen, se realiza la compra
            cliente.realizar_compra(producto, cantidad)
        else:
            print("Cliente o producto no encontrado") #si no se encuentran, se imprime un mensaje de error

    def mostrar_productos(self):
        for p in self.lista_productos_disponibles:
            p.mostrar_info()
    
    def mostrar_clientes(self):
        for c in self.lista_clientes_registrados:
            c.mostrar_info()

    def guardar_datos(self, archivo: str):
        with open(archivo, "w") as f:
            f.write("Productos\n")
            for p in self.lista_productos_disponibles:
                f.write(f"{p.nombre},{p.id},{p.precio},{p.cantidad}\n")
            f.write("Clientes\n")
            for c in self.lista_clientes_registrados:
                f.write(f"{c.nombre},{c.id},{c.saldo}\n")
    
    def cargar_datos(self, archivo: str):
        with open(archivo, "r") as f:
            lineas = f.readlines() #se lee el archivo y se guardan las lineas en una lista
            tipo = None #se inicializa la variable tipo
            for l in lineas: #se recorre la lista de lineas
                if l == "Productos\n": #si la linea es igual a "Productos\n", se cambia el tipo a "Productos"
                    tipo = "Productos" 
                elif l == "Clientes\n": #si la linea es igual a "Clientes\n", se cambia el tipo a "Clientes"
                    tipo = "Clientes"
                else:
                    if tipo == "Productos": #si el tipo es "Productos", se crean los productos con los datos de la linea
                        datos = l.strip().split(",")
                        producto = Producto(datos[0], int(datos[1]), float(datos[2]), int(datos[3]))
                        self.lista_productos_disponibles.append(producto)
                    elif tipo == "Clientes": #si el tipo es "Clientes", se crean los clientes con los datos de la linea
                        datos = l.strip().split(",")
                        cliente = Cliente(datos[0], int(datos[1]), float(datos[2]))
                        self.lista_clientes_registrados.append(cliente)