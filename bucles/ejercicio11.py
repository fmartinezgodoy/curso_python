

palabra_usuario = input("Ingrese una palabra: ")

for i in range(len(palabra_usuario)):
    index = len(palabra_usuario) - i
    print(palabra_usuario[index-1])
