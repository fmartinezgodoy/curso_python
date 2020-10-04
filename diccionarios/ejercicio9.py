
facturas = {}
cantidad_cobrada = 0
deuda_total = 0

while True:
    opcion = int(input("Desea añadir una nueva factura, pagar una existente "
             "o finalizar el proceso? (ingrese 1, 2 o 3):"))

    if opcion == 1:
        facturas.setdefault(input("Ingrese el número de la factura: "),
                                  float(input("Ingrese el coste de la factura: ")))

    elif opcion == 2:
        cantidad_cobrada += facturas.pop(input("Ingrese el número de la factura a pagar: "))
        
    elif opcion == 3:
        break

    print("Se han cobrado ${} hasta el momento...".format(cantidad_cobrada))

    for factura,deuda in facturas.items():
        deuda_total += deuda

    print("Se debe un total de ${}".format(deuda_total))

    deuda_total = 0
