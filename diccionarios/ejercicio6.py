user = {}
quit = False

while not quit:
    key = input("Ingrese una característica: ")
    value = input("Ingrese el valor de esa característica: ")

    user[key] = value

    print(user)
    
    if input("Ingresar otra? [s/n]: ") != "s":
        quite = True
