breadPrice = 3.49
discount = 0.6

oldBreadAmount = float(input("Ingrese la cantidad de barras vendidas de ayer: "))

regularPrice = breadPrice * oldBreadAmount
specialPrice = regularPrice * (1 - discount)

print("El precio de una barra de pan es de ${}.".format(
    round(breadPrice)
    )
)
print(
    "El descuento del pan por no ser fresco es de ${}.".format(
        round(breadPrice * (1 - discount))
    )
)
print("Costo final: " + str(round(specialPrice, 1)))
