

nombre_usuario = input("Ingrese su nombre: ")
sexo_usuario = input("Ingrese su sexo: ")


if sexo_usuario[0] == "m":
    if nombre_usuario[0] > "n":
        print("Pertecene al grupo A")
    else:
        print("Pertenece al grupo B")

elif sexo_usuario[0] == "f":
    if nombre_usuario[0] < "m":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

else:
    print("Error, ingrese un sexo correcto (femenino/masculino)")

    