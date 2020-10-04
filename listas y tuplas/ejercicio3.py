


asignaturas = ["Matemática", "Física", "Historia", "Química", "Lengua"]
notas = []

for i in range(len(asignaturas)):

    nota_asignatura = float(input("Ingrese la nota obtenida en la asignatura " + asignaturas[i] + ":"))

    notas.append(nota_asignatura)

for i in range(len(asignaturas)):

    print("En la asignatura " + asignaturas[i] + " ha sacado " + str(round(notas[i],1)))










