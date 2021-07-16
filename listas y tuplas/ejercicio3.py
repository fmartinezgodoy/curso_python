courses = ["Matemática", "Física", "Química", "Historia", "Lengua"]

grades = []

for course in courses:
    grade = input("Que nota sacaste en {}?: ".format(course))
    grades.append(grade)

for course, grade in map(lambda c,g : [c,g], courses, grades):
    print("En {} has sacado {}.".format(course, grade))
