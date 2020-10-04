

asignaturas = ["Matemática", "Física", "Historia", "Química", "Lengua"]

print("Yo estudio: ", end = "")
for i in range(len(asignaturas)):
    if i != (len(asignaturas)-1):
        print(asignaturas[i] + ",", end = " ")
    else:
        print(asignaturas[i])



