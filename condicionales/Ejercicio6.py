name = input("Ingrese su nombre: ")
gender = input("Ingrese su sexo: ")

if gender[0] == "m":
    if name[0] > "n":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")

else:
    if name[0] < "m":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
