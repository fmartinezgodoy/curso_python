
sys_pass = "contraseña"
pass_confirm = 0

while pass_confirm == 0:

    pass_check = str.lower(input("Ingrese una contraseña: "))
    print("")

    if pass_check == sys_pass:
        pass_confirm = 1
        print("Contraseña aceptada.")
    else:
        print("Contraseña incorrecta.")
        print("")


