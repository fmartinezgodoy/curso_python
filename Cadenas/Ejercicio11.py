product = input('Ingrese el nombre del producto: ')
price = input('Ingrese el precio del producto: ')
qty = input('Ingrese la cantidad: ')
print(
    "{name} {unitPrice:6.2f} {units:3d} {totalPrice:8.2f}".format(
        name=product,
        unitPrice=float(price),
        units=int(qty),
        totalPrice=float(price)*float(qty)
    )
)
