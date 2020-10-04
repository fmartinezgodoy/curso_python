


numero_usuario = int(input("Ingrese un número entero: "))

check = True
newcheck = True
i = 2

while check == True:

    print(str(i))


    if numero_usuario % (i) == 0:
        print("El número no es primo")
        check = False
        newcheck = False

    if i == numero_usuario-1:
        check = False

    i = i + 1

if newcheck == True:
    print("El número es primo")








