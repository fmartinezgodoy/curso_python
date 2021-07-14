age = int(input("Ingrese edad del cliente: "))

if age < 4:
    price = 0
elif age > 18:
    price = 10
else:
    price = 5

print("El precio de la entrada es: {}€.".format(str(price)))
