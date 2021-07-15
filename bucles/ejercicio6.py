num = int(input("Ingrese un número entero: "))

for i in range(num):
    line = ""
    for e in range(i+1):
        line += '*'
    print(line)
