
informacion = {}

while True:
    informacion.setdefault(input("Ingrese una característica: "), input("Ingrese el valor de esa característica: "))
    print(informacion)
    if input("Ingresar otra? y/n:") == "n":
        break


