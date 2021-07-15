num = int(input("Ingrese un número entero: "))

isPrime = True
i = 2

while isPrime and i < num:
    if num % (i) == 0:
        isPrime = False
    i += 1

print("El número ingresado {}es primo.".format("" if isPrime else "no "))
