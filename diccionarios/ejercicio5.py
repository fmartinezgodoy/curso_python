data = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

acc = 0

for subject,credits in data.items():
    acc += credits
    print("{} tiene {} créditos".format(subject, credits))

print("El número total es {} créditos.".format(acc))
