


cantidad_inversion = float(input("Ingrese la cantidad a invertir: "))

interes_anual = float(input("Ingrese el valor del interés anual: "))

numero_anos = int(input("Ingrese la cantidad de años que dura la inversión: "))

for i in range(numero_anos):
    cantidad_inversion = round(cantidad_inversion*(1+interes_anual),2)
    print("El capital obtenido durante el año " + str(i+1) + " es de: $" + str(cantidad_inversion))








