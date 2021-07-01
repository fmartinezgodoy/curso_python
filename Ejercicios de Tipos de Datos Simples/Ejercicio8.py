n = int(input("Ingrese el primer numero entero: "))
m = int(input("Ingrese el segundo número entero: "))
c = n / m
r = n % m

print(
    "{n} entre {m} da un cociente {c} y un resto {r}.".format(
        n=n, m=m, c=c, r=r
    )
)
