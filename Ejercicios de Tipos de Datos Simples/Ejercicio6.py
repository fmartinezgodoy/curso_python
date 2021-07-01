n = int(input('Ingrese un entero positivo: '))
result = n * (n + 1) / 2
print(
    'El resultado de sumar los primeros {n} números positivos es {result}.'.format(
        n=n, result=result
    )
)
