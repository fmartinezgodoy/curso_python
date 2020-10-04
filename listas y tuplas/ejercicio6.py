

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for i in range(len(asignaturas)):
    nota = round(float(input("Ingrese la nota obtenida en la asignatura {}: ".format(asignaturas[i]))),1)

    notas.append(nota)

i = 0

while True:
    if i != len(asignaturas):
        if notas[i] >= 7:
            asignaturas.pop(i)
            notas.pop(i)
            i = i - 1
        i += 1
    else:
        break


print("Las asignaturas que debe repetir son: {}".format(asignaturas))




