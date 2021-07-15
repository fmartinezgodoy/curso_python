num = int(input("Ingrese un número entero: "))

for i in range(num+1):
    if i%2 != 0:
        line = ""
        for c in range(i+1, 0, -1):
            if c%2 != 0:
                line += "{} ".format(c)
        print(line)
