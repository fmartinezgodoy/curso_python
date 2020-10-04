lista_compra = {}
precio_total = 0


while True:
    lista_compra.setdefault(input("Articulo: "),int(input("Precio: ")))


    if input("Otro articulo? y/n: ") == "n":
        break

for articulo,precio in lista_compra.items():
    print("{:16}".format(articulo),end ="")
    print("{:>16}".format(precio))
    precio_total += precio

print("{:16}".format("..."),end ="")
print("{:>16}".format("..."))

print("{:16}".format("Total"),end ="")
print("{:>16}".format(precio_total))

