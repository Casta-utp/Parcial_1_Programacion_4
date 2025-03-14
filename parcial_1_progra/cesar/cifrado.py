class CifradoCesar:
    lista_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista_minusculas = lista_mayusculas.lower()
    lista_mensajes = []

    def __init__(self, mensaje, desplazamiento, cifrado):
        self.mensaje = mensaje
        self.desplazamiento = desplazamiento
        self.cifrado = cifrado

    def cifrar(self, mensaje, desplazamiento):
        mensaje_cifrado = ""
        for letra in mensaje:
            if letra in self.lista_mayusculas:
                indice = self.lista_mayusculas.index(letra)
                mensaje_cifrado += self.lista_mayusculas[(indice + desplazamiento) % len(self.lista_mayusculas)]
            elif letra in self.lista_minusculas:
                indice = self.lista_minusculas.index(letra)
                mensaje_cifrado += self.lista_minusculas[(indice + desplazamiento) % len(self.lista_minusculas)]
            else:
                mensaje_cifrado += letra  # Mantiene espacios, números y símbolos sin cambios
        self.lista_mensajes.append(mensaje_cifrado)
        print(mensaje_cifrado)
        return mensaje_cifrado

    def descifrar(self, mensaje, desplazamiento):
        mensaje_descifrado = ""
        for letra in mensaje:
            if letra in self.lista_mayusculas:
                indice = self.lista_mayusculas.index(letra)
                mensaje_descifrado += self.lista_mayusculas[(indice - desplazamiento) % len(self.lista_mayusculas)]
            elif letra in self.lista_minusculas:
                indice = self.lista_minusculas.index(letra)
                mensaje_descifrado += self.lista_minusculas[(indice - desplazamiento) % len(self.lista_minusculas)]
            else:
                mensaje_descifrado += letra  # Mantiene espacios, números y símbolos sin cambios
        print(mensaje_descifrado)
        return mensaje_descifrado

    def descifrar_lista(self, index, desplazamiento):
        if 0 <= index < len(self.lista_mensajes):
            mensaje = self.lista_mensajes[index]
            return self.descifrar(mensaje, desplazamiento)
        else:
            print("Índice fuera de rango")
            return None
    
    def __str__(self):
        return f"Mensaje: {self.mensaje}, Desplazamiento: {self.desplazamiento}, Cifrado: {self.cifrado}"
    
    def guardar_lista(self):
        with open("mensajes.txt", "w") as archivo:
            for mensaje in self.lista_mensajes:
                archivo.write(mensaje + "\n")
        print("Lista de mensajes guardada en mensajes.txt")
    
    def cargar_lista(self):
        try:
            with open("mensajes.txt", "r") as archivo:
                self.lista_mensajes = [line.strip() for line in archivo.readlines()]
            print("Lista de mensajes cargada de mensajes.txt")
        except FileNotFoundError:
            print("No se encontró mensajes.txt. Asegúrese de guardar mensajes primero.")
