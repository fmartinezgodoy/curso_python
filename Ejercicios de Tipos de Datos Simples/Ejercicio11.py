interest = 0.04
investment = int(
    input(
        'Ingrese la cantidad de dinero depositada en la cuenta de ahorro:'
    )
)

investment *= (1 + interest)
print(
    "Ahorros tras el primer año: ${}.".format(
        round(investment, 2)
    )
)
investment *= (1 + interest)
print(
    "Ahorros tras el segundo año: ${}.".format(
        round(investment, 2)
    )
)
investment *= (1 + interest)
print(
    "Ahorros tras el tercer año: ${}.".format(
        round(investment, 2)
    )
)
