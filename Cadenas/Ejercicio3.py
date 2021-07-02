name = input('Ingrese su nombre: ')
n = len(name)
print(
    "{name} tiene {n} letras".format(name=name.upper(), n=n)
)
