def bin2dec(numero):

    numero = int(str(numero),2)
    return numero

def dec2bin(numero):

    numero = int(bin(numero)[2:])

    return numero


numero = int(input("Ingrese un número entero: "))

numero = dec2bin(numero)

print(numero)

numero = bin2dec(numero)

print(numero
      