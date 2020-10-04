def frecuencia(string):
    dict = {}
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict.setdefault(string[i], 1)

    return dict

def frecuente(dict):
    mayor = 0
    for palabra, frecuencia in dict.items():
        if frecuencia > mayor:
            mayor = frecuencia
            dato = (palabra, frecuencia)

    return dato


string = input("Ingrese una frase: ")
palabras = frecuencia(string.split(" "))

mayor = frecuente(palabras)
print(palabras)
print(mayor)

