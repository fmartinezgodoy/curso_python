

system_password = "contraseña"


user_password = str.lower(input("Ingrese su contraseña: "))

if user_password == system_password:
    print("La contraseña ingresada es correcta.")
else:
    print("La contraseña ingresada es incorrecta.")


