
traductor = {}

while True:
    par = input("Ingrese par <palabra>:<traducción>: ").split(":")
    traductor.setdefault(par[0], par[1])

    if input("Ingresar otra palabra? y/n: ") == "n":
        break

frase = input("Introduzca una frase: ")
frase = frase.split(" ")

for palabra in frase:
    print(traductor.get(palabra, "#"),end=" ")

