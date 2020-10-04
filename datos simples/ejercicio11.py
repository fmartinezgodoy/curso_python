


invert = float(input("Ingrese la cantidad a invertir: "))
interes =  float(input("Ingrese el interés anual de su inversión: "))
anos = float(input("Ingrese la cantidad de años que durará la inversión :"))

rent = (invert*(1+interes)**anos)

print ("El capital obtenido es " + str(round(rent,2)))