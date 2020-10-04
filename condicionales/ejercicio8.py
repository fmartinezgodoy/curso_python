


puntuacion_empleado = float(input("Ingrese la puntuación del empleado: "))

if puntuacion_empleado == 0.0:
    rendimiento_empleado = "Inaceptable"
elif puntuacion_empleado == 0.4:
    rendimiento_empleado = "Aceptable"
else:
    rendimiento_empleado = "Meritorio"

print("El rendimiento del empleado es: " + rendimiento_empleado)
dinero_empleado = round(puntuacion_empleado * 2400,2)
print("La cantidad de dinero correspondiente es: " + str(dinero_empleado))









