

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
lista_alfabeto = []

i = 0

while True:

    lista_alfabeto.append(alfabeto[i])

    if alfabeto[i] == "l":
        lista_alfabeto.append("ll")

    i += 1

    if i == len(alfabeto):
        break

for i in range(len(lista_alfabeto), 1, -1):
    if i%3 == 0:
        lista_alfabeto.pop(i-1)

print(lista_alfabeto)
