


numeros = []

while True:

    numero = int(input("Ingrese un número ganador de la loteria: "))

    numeros.append(numero)

    check = input("Desea ingresar otro número: ")

    if check == "no":
        print("")
        print("Terminando carga de números.")
        print("")
        break
    else:
        print("")
        print("Ok!")
        print("")

numeros.sort()

print(numeros)














