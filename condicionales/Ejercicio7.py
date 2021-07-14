annualRent = float(input("Ingrese el valor de su renta anual: "))

if annualRent < 10000:
    tax = '5'
elif annualRent < 20000:
    tax = '15'
elif annualRent < 35000:
    tax = '20'
elif annualRent < 60000:
    tax = '30'
else:
    tax = '45'

print('Le corresponde un tipo impositivo de {}%.'.format(tax))
