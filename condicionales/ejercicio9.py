



edad_cliente = int(input("Ingrese edad del cliente: "))


if edad_cliente < 4:
    precio_entrada = 0
elif edad_cliente >=4 and edad_cliente <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

print("El precio de la entrada es: " + str(precio_entrada))