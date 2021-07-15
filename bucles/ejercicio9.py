secret = "contraseña"
logged = False

while not logged:
    pwd = str.lower(input("Ingrese una contraseña: "))
    if pwd == secret:
        logged = True
        print("Bienvenido.")
    else:
        print("Contraseña incorrecta.")
