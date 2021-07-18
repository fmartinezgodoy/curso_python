bills = {}
amountPaid = 0
debt = 0
quit = False

while not quit:
    option = int(input("Desea añadir una nueva factura, pagar una existente "
             "o finalizar el proceso? [1/2/3]: "))

    if option == 1:
        num = input("Ingrese el número de la factura: ")
        cost = float(input("Ingrese el coste de la factura: $"))
        bills[num] = cost
        debt += cost

    elif option == 2:
        toPay = input("Ingrese el número de la factura a pagar: ")
        if toPay in bills:
            cost = bills.pop(toPay)
            amountPaid += cost
            debt -= cost
        else:
            print("El número ingresado no corresponde a una factura.")

    elif option == 3:
        quit = True

    print("Se han cobrado ${} hasta el momento...".format(amountPaid))
    print("Se debe un total de ${}".format(debt))
