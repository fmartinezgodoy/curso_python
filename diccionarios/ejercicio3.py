prices = {"Plátano" : 1.35, "Manzana" : 0.8, "Pera" : 0.85, "Naranja" : 0.7}

selected = input("Ingrese una fruta: ")

if selected in prices:
    qty = float(input("Ingrese la cantidad en kilos: "))
    message = "Debe abonar ${}".format(round(prices.get(selected)*qty, 2))
else:
    message = "La fruta no está disponible."

print(message)
