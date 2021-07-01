clownWeight = 112
dollWeight = 75

clownAmount = float(input("Ingrese cantidad de payasos vendidos: "))
dollAmount = float(input("Ingrese cantidad de muñecas vendidas: "))

weight = clownAmount * clownWeight + dollAmount * dollWeight

print(
    'El peso total es {}g.'.format(
        round(weight)
    )
)
