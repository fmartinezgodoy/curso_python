clientes = {}

while True:
    opcion_menu = int((input("Elija una de las siguientes opciones...\n"
                             "(1) Añadir cliente,\n"
                             "(2) Eliminar cliente,\n"
                             "(3) Mostrar cliente,\n"
                             "(4) Listar todos los clientes,\n"
                             "(5) Listar clientes preferentes,\n"
                             "(6) Terminar \n"
                             "Ingrese elección: ")))

    if opcion_menu == 1:
        clientes.setdefault(input("Ingrese NIF del cliente: "),
                            {"nombre" : input("Ingrese nombre del cliente: "),
                             "dirección" : input("Ingrese dirección del cliente: "),
                             "teléfono" : input("Ingrese teléfono del cliente: "),
                             "correo" : input("Ingrese correo del cliente: "),
                             "preferente" : bool(input("Cliente preferente? (True/False)"))})

    elif opcion_menu == 2:
        clientes.pop(input("Ingrese NIF del cliente: "))

    elif opcion_menu == 3:
        print(clientes[input("Ingrese NIF del cliente: ")])

    elif opcion_menu == 4:
        for NIF, info in clientes.items():
            print(NIF, info["nombre"])

    elif opcion_menu == 5:
        for NIF, info in clientes.items():
            if info["preferente"] == True:
                print(NIF, info["nombre"])

    elif opcion_menu == 6:
        break

    print("")
    input("Presione enter para continuar")
    print("")

