cart = {}
quit = False
total = 0

while not quit:
    prod = input("Articulo: ")
    price = input("Precio: ")

    cart[prod] = price
    total += int(price)

    if input("Otro articulo? [s/n]: ") != "s":
        quit = True

for prod, price in cart.items():
    print("{:16}\t{}".format(prod, price))

print("{:16}\t{}".format("...", "..."))
print("{:16}\t{}".format("Total",total))
