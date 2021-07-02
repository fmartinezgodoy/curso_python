price = input('Ingrese el precio en euros: ')
euros = price[:price.find('.')]
cents = price[price.find('.')+1:]
print("Euros: {e}; céntimos: {c}.".format(e=euros, c=cents))
