

palabra_usuario = input("Ingrese una palabra: ")

lista_letras_palabra=[]
check = True

print(palabra_usuario)

for i in range(len(palabra_usuario)):
    lista_letras_palabra.append(palabra_usuario[i])

print(lista_letras_palabra)

if len(lista_letras_palabra)%2 == 0:
    for i in range(int(len(lista_letras_palabra)/2)):
        if lista_letras_palabra[i] != lista_letras_palabra[-i-1]:
            check = False
            break
else:
    for i in range(int((len(lista_letras_palabra)-1)/2)):
        if lista_letras_palabra[i] != lista_letras_palabra[-i-1]:
            check = False
            break

if check == True:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")


