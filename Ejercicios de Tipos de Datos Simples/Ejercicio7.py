weight = int(input("Ingrese su peso (en kg): "))
height = int(input("Ingrese su altura (en metros): "))
result = weight / height

print(
    "Tu índice de masa corporal es {}.".format(
        round(result, 2)
    )
)
