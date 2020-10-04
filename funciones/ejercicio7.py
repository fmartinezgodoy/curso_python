
def cuadrados(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]**2

    return lista

print(cuadrados([2,2,2,2]))
