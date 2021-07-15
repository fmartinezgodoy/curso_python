amount = float(input("Ingrese la cantidad a invertir: "))
interest = float(input("Ingrese el valor del interés anual: "))
years = int(input("Ingrese la cantidad de años que dura la inversión: "))

for i in range(years):
    amount = round(amount*(1+interest),2)
    print(
        "El capital obtenido durante el año {} es de: ${}".format(
            str(i+1), 
            str(amount)
        )
    )
