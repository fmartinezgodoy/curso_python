import math

lista_numeros = input("Ingrese una lista de números separados por coma: ")

lista_diferencia = []

lista_numeros = lista_numeros.split(",")

acumulador = 0
for i in range(len(lista_numeros)):
    lista_numeros[i] = float(lista_numeros[i])

media = sum(lista_numeros) / len(lista_numeros)

for i in range(len(lista_numeros)):
    lista_diferencia.append(lista_numeros[i] - media)

acumulador = 0
for i in range(len(lista_diferencia)):
    acumulador += lista_diferencia[i]**2

dev_est = math.sqrt(acumulador/len(lista_numeros))

print("La desviación estandar es {}.".format(round(dev_est,2)))








