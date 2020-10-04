divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa_usuario = input("Ingrese una divisa: ")

if divisa_usuario in divisas:
    print(divisas.get(divisa_usuario))
else:
    print("No esta disponible")