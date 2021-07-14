score = float(input("Ingrese la puntuación del empleado: "))

if score == 0.0:
    performance = "Inaceptable"
elif score == 0.4:
    performance = "Aceptable"
else:
    performance = "Meritorio"

print("El rendimiento del empleado es: " + performance)
pay = round(score * 2400, 2)
print("La cantidad de dinero correspondiente es: " + str(pay))
