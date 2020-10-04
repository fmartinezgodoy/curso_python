


eleccion_principal = input("Ingrese si desea una pizza vegetariana o no vegetariana: ")

if eleccion_principal[0] == "v":
    print("Las opciones para ingredientes de su pizza son: ")
    print("-Pimiento")
    print("-Tofu")
elif eleccion_principal[0] == "n":
    print("Las opciones para ingredientes de su pizza son: ")
    print("-Peperoni")
    print("-Jamón")
    print("-Salmón")

eleccion_ingrediente = input("Ingrese su elección de ingrediente: ")

print("Su pizza será " + eleccion_principal + " con el ingrediente " + eleccion_ingrediente + " como adicional sumado a la mozzarella y el tomate.")




