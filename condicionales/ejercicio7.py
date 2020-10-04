

renta_usuario = float(input("Ingrese el valor de su renta anual: "))

if renta_usuario < 10000:
    print("El tipo impositivo correspondiente es 5%.")
elif renta_usuario >= 10000 and renta_usuario < 20000:
    print("El tipo impositivo correspondiente es 15%.")
elif renta_usuario >= 20000 and renta_usuario < 35000:
    print("El tipo impositivo correspontiente es 20%.")
elif renta_usuario >= 35000 and renta_usuario < 60000:
    print("El tipo impositivo correspondiente es 30%.")
else:
    print("El tipo impositivo correspondiente es 45%.")


