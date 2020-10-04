precios = {"Plátano" : 1.35, "Manzana" : 0.8, "Pera" : 0.85, "Naranja" : 0.7}

fruta = input("Ingrese una fruta: ")
cantidad = float(input("Ingrese la cantidad en kilos: "))

try:
    costo = precios.get(fruta) * cantidad
    print("Debe abonar ${}".format(costo))
except:
    print("La fruta ingresada no esta disponible.")