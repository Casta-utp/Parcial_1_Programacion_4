from cifrado import CifradoCesar

def menu():
    print("Bienvenido al cifrado César")
    cifrado_cesar = CifradoCesar("", 0, "")  # Se mantiene una única instancia
    cifrado_cesar.cargar_lista()  # Cargar mensajes previos al iniciar

    while True:
        print("\n1. Cifrar un mensaje")
        print("\n2. Descifrar un mensaje")
        print("\n3. Descifrar un mensaje de la lista")
        print("\n4. Guardar lista de mensajes")
        print("\n5. Cargar lista de mensajes")
        print("\n6. Mostrar lista de mensajes")
        print("\n7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje = input("Introduzca el mensaje a cifrar: ")
            desplazamiento = int(input("Introduzca el desplazamiento: "))
            mensaje_cifrado = cifrado_cesar.cifrar(mensaje, desplazamiento)
            print(f"Mensaje cifrado: {mensaje_cifrado}")

        elif opcion == "2":
            mensaje = input("Introduzca el mensaje a descifrar: ")
            desplazamiento = int(input("Introduzca el desplazamiento: "))
            mensaje_descifrado = cifrado_cesar.descifrar(mensaje, desplazamiento)
            print(f"Mensaje descifrado: {mensaje_descifrado}")

        elif opcion == "3":
            index = int(input("Introduzca el índice del mensaje a descifrar: "))
            desplazamiento = int(input("Introduzca el desplazamiento: "))

            if len(cifrado_cesar.lista_mensajes) == 0:
                print("No hay mensajes en la lista. Cargue mensajes o cifre uno primero.")
            elif 0 <= index < len(cifrado_cesar.lista_mensajes):
                cifrado_cesar.descifrar_lista(index, desplazamiento)
            else:
                print("Índice fuera de rango.")

        elif opcion == "4":
            cifrado_cesar.guardar_lista()

        elif opcion == "5":
            cifrado_cesar.cargar_lista()

        elif opcion == "6":
            if len(cifrado_cesar.lista_mensajes) == 0:
                print("La lista de mensajes está vacía.")
            else:
                print("\nMensajes almacenados:")
                for i, mensaje in enumerate(cifrado_cesar.lista_mensajes):
                    print(f"{i}. {mensaje}")

        elif opcion == "7":
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

    print("Gracias por usar el cifrado César")

if __name__ == "__main__":
    menu()