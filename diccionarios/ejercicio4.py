
fecha = {"Día" : "", "Mes" : "", "Año" : ""}

fecha_usuario = input("Ingrese la fecha en formato dd/mm/aaaa: ").split("/")


fecha["Día"] = fecha_usuario[0]
fecha["Mes"] = fecha_usuario[1]
fecha["Año"] = fecha_usuario[2]

print("{} de {} de {}".format(fecha.get("Día"),fecha.get("Mes"),fecha.get("Año")))