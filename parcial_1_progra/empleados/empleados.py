class Empleados:

    def __init__(self, nombre, id, salario_base, experiencia):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base
        self.experiencia = experiencia #La experiencia se da en años
    
    def __str__ (self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Salario base: {self.salario_base}, Antiguedad: {self.experiencia}"
    
    def calcular_salario(self):
        if self.experiencia >= 0 and self.experiencia <= 2:
            return self.salario_base + (self.salario_base * 0.05)
        elif self.experiencia >= 3 and self.experiencia <= 5:
            return self.salario_base + (self.salario_base * 0.1)
        elif self.experiencia > 5:
            return self.salario_base + (self.salario_base * 0.15)
        else:
            return "Introduzca un valor valido para los años de experiencia"
        

class GestorEmpleados:

    lista_empleados = []

    def agregar_empleado(self, empleado: Empleados):
        self.lista_empleados.append(empleado)

    def eliminar_empleado(self, id):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                self.lista_empleados.remove(empleado)
                print(f"Empleado con ID {id} eliminado")
            else :
                print(f"No se encontro empleado con ID {id}")

    def buscar_empleado(self, id: int):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                print(empleado)
            else:
                print(f"No se encontro empleado con ID {id}")
        
    def modificar_empleado(self, id: int, nombre: str, salario_base: float, experiencia: int):
        for empleado in self.lista_empleados:
            if empleado.id == id:
                empleado.nombre = nombre
                empleado.salario_base = salario_base
                empleado.experiencia = experiencia
                print(f"Empleado con ID {id} modificado")
            else:
                print(f"No se encontro empleado con ID {id}")

    def mostrar_empleados (self):
        for empleado in self.lista_empleados:
            print(empleado)
    
    def guardar_empleados(self):
        with open("empleados.txt", "w") as archivo:
            for empleado in self.lista_empleados:
                archivo.write(f"{empleado.nombre},{empleado.id},{empleado.salario_base},{empleado.experiencia}\n")
    
    def cargar_empleados(self):
        with open("empleados.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",") #strip() elimina los espacios en blanco al inicio y al final de la linea
                empleado = Empleados(datos[0], datos[1], datos[2], datos[3]) #datos[0] es el nombre, datos[1] es el id, datos[2] es el salario base, datos[3] es la experiencia
                self.lista_empleados.append(empleado) #Agregamos el empleado a la lista de empleados