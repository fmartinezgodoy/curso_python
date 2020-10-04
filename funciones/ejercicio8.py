import numpy

def numeros(lista):
    media = sum(lista)/len(lista)
    varianza = numpy.var(lista)
    desv_est = numpy.std(lista)

    numeros = {"media" : media, "varianza" : varianza, "desviación estandar" : desv_est}

    return numeros

numeros = numeros([2, 3, 4, 5, 6, 7, 7, 7, 7 ,7, 8, 8, 9, 10])

print(numeros["media"])
print(numeros["varianza"])
print(numeros["desviación estandar"])