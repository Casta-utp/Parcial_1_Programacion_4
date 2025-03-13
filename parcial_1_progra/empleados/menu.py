from empleados import Empleados, GestorEmpleados

def menu():
    print("Bienvenido al sistema de empleados")
    gestor = GestorEmpleados()
    while True:
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado")
        print("4. Modificar empleado")
        print("5. Mostrar empleados")
        print("6. Guardar empleados")
        print("7. Cargar empleados")
        print("8. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del empleado: ")
            id = int(input("Ingrese el ID del empleado: "))
            salario_base = float(input("Ingrese el salario base del empleado: "))
            experiencia = int(input("Ingrese la experiencia del empleado en años: "))
            empleado = Empleados(nombre, id, salario_base, experiencia)
            gestor.agregar_empleado(empleado)
        elif opcion == 2:
            id = int(input("Ingrese el ID del empleado a eliminar: "))
            gestor.eliminar_empleado(id)
        elif opcion == 3:
            id = int(input("Ingrese el ID del empleado a buscar: "))
            gestor.buscar_empleado(id)
        elif opcion == 4:
            id = int(input("Ingrese el ID del empleado a modificar: "))
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            salario_base = float(input("Ingrese el nuevo salario base del empleado: "))
            experiencia = int(input("Ingrese la nueva experiencia del empleado en años: "))
            gestor.modificar_empleado(id, nombre, salario_base, experiencia)
        elif opcion == 5:
            gestor.mostrar_empleados()
        elif opcion == 6:
            gestor.guardar_empleados()
        elif opcion == 7:
            gestor.cargar_empleados()
        elif opcion == 8:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()

    

        