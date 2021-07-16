subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grades = []

for subject in subjects:
    nota = round(float(input("Ingrese la nota obtenida en la asignatura {}: ".format(subject))),1)
    grades.append(nota)

for grade in grades:
    if grade > 6:
        i = grades.index(grade)
        subjects.pop(i)
        grades.pop(i)

print("Las asignaturas que debe repetir son: {}".format(subjects))
