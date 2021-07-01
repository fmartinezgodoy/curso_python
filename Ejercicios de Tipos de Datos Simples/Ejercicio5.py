hoursWorked = float(input('Ingrese la cantidad de horas trabajadas: '))
hourlyWage = float(input('Ingrese su paga por hora: '))
print(
    'Le corresponden ${} por las horas trabajadas.'.format(
        round(hoursWorked*hourlyWage, 2)
    )
)
