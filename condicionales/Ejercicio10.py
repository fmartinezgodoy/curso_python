if input("Desea una pizza vegetariana?[s/n]:") == 's':
    vegetarian = True
else:
    vegetarian = False

if vegetarian:
    print('Las opciones para ingredientes de su pizza son: \n -Pimiento \n -Tofu')
else:
    print("Las opciones para ingredientes de su pizza son: \n -Peperoni \n -Jamón \n -Salmón")

ingredient = input("Ingrese su elección de ingrediente: ")

print(
    "Su pizza será {vegetarian} con {ingredient}, mozzarella y tomate.".format(
        vegetarian="Vegetariana" if vegetarian else "no vegetariana",
        ingredient=ingredient
    )
)
