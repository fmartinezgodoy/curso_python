

numero_usuario = int(input("Ingrese un número entero: "))


for i in range(numero_usuario+1):
    if i%2 != 0:
        a = i+1
        for c in range(i+1):

            if c%2 != 0:

                if c != i:
                    print(str(a), end = " ")
                else:
                    print(str(a))

            a = a - 1




