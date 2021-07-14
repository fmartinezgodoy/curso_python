secret = "contraseña"


password = str.lower(input("Ingrese su contraseña: "))

if password == secret:
    print("La contraseña ingresada es correcta.")
else:
    print("La contraseña ingresada es incorrecta.")
