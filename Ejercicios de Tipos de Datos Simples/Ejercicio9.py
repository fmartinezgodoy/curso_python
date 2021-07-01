investment = float(input("Ingrese la cantidad que desea invertir: "))
interest = float(input("Ingrese el interés anual de su inversión (en %): "))
years = float(input("Ingrese la cantidad de años que durará la inversión: "))

result = investment * (1 + interest/100)**years

print(
    "El capital esperado es de ${}.".format(result)
)
