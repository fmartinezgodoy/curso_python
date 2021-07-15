num = int(input("Ingrese un número entero: "))

for i in range(num+1):
    if i%2 != 0:
        print(str(i), end = ", ")
