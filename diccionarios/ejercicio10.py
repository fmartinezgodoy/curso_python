clientes = {}
quit = False

while not quit:
    option = int((input("Elija una de las siguientes opciones...\n"
                             "\t(1) Añadir cliente,\n"
                             "\t(2) Eliminar cliente,\n"
                             "\t(3) Mostrar cliente,\n"
                             "\t(4) Listar todos los clientes,\n"
                             "\t(5) Listar clientes preferentes,\n"
                             "\t(6) Terminar \n"
                             "Ingrese elección: ")))

    if option == 1:
        nif = input("Ingrese NIF del cliente: ")
        clientes[nif] = {
                "Nombre" : input("Ingrese nombre del cliente: "),
                "Dirección" : input("Ingrese dirección del cliente: "),
                "Teléfono" : input("Ingrese teléfono del cliente: "),
                "Email" : input("Ingrese correo del cliente: "),
                "Preferente" : input("Cliente preferente? (s/n): ") == 's',
            }

    elif option == 2 or option == 3:
        nif = input("Ingrese NIF del cliente: ")
        if nif in clientes:
            if option == 2:
                message= "Eliminado correctamente."
            elif option == 3:
                details = str(clientes[nif])
                details = details[1:len(details)-1]
                message = ""
                for word in details.split(', '):
                    message += "{}\n".format(word)
            else:
                message = "La opción ingresada no es correcta."
        else:
            message = "El NIF ingresado no es correcto."
        print(message)

    elif option == 4 or option == 5:
        message = ""
        for nif, data in clientes.items():
            if option == 4:
                message += "{:16}\t{}\n".format(nif, data["Nombre"])
            elif option == 5:
                if data["Preferente"] == True:
                    message += "{:16}\t{}\n".format(nif, data["Nombre"])
            else:
                message = "La opción ingresada no es correcta."
        print(message)

    elif option == 6:
        quit = True
    
    input("\nPresione enter para continuar...\n")
