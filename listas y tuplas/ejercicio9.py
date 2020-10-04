

palabra_usuario = input("Ingrese una palabra: ")

lista_letras = [0,0,0,0,0] # a,e,i,o,u

for i in range(len(palabra_usuario)):
    if palabra_usuario[i] == "a":
        lista_letras[0] += 1
    elif palabra_usuario[i] == "e":
        lista_letras[1] += 1
    elif palabra_usuario[i] == "i":
        lista_letras[2] += 1
    elif palabra_usuario[i] == "o":
        lista_letras[3] += 1
    elif palabra_usuario[i] == "u":
        lista_letras[4] += 1

print("La letra a aparece {} veces, e {} veces, i {} veces, "
      "o {} veces, u {} veces.".format(lista_letras[0], lista_letras[1],
                                       lista_letras[2], lista_letras[3],
                                       lista_letras[4]))
