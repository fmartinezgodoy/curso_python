


frase_usuario = input("Ingrese una frase: ")
letra_usuario = input("Ingrese una letra: ")

count = 0

for i in range(len(frase_usuario)):

    if frase_usuario[i] == letra_usuario:
        frase_usuario[i]
        count = count + 1


print("La letra " + letra_usuario + " aprece " + str(count) + " en la frase.")