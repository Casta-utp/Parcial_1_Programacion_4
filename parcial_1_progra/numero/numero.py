# a = 5691 % 10 # 0
# b = 5690 // 10 % 10 # 9
# c = 5690 // 100 % 10 # 6
# d = 5690 // 1000 % 10 # 5

# print(a)

# print(b)

# print(c)

# print(d)

#a multiplo de b?

def entrada():
    while True:
        numero = int(input("Ingrese un numero de 4 cifras: "))
        if numero >= 1000 and numero <= 9999:
            break
        else:
            print("Numero invalido")
    return numero

def descomponer_numero(numero):
    primera_cifra = numero // 1000 % 10
    segunda_cifra = numero // 100 % 10
    tercera_cifra = numero // 10 % 10
    cuarta_cifra = numero % 10
    return primera_cifra, segunda_cifra, tercera_cifra, cuarta_cifra

def es_multiplo(primera_cifra, cuarta_cifra):
    if primera_cifra % cuarta_cifra == 0:
        print(f"{primera_cifra} es multiplo de {cuarta_cifra}")
    else:
        print(f"{primera_cifra} no es multiplo de {cuarta_cifra}")

def suma_cifras(segunda_cifra, tercera_cifra):
    suma = segunda_cifra + tercera_cifra
    print(f"La suma de {segunda_cifra} y {tercera_cifra} es {suma}")

def main():
    numero = entrada()
    primera_cifra, segunda_cifra, tercera_cifra, cuarta_cifra = descomponer_numero(numero)
    es_multiplo(primera_cifra, cuarta_cifra)
    suma_cifras(segunda_cifra, tercera_cifra)

main()