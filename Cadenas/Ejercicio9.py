birthdate = input('Ingrese la fecha de su nacimiento: ')
day = birthdate[:birthdate.find('/')]
left = birthdate[birthdate.find('/')+1:]
month = left[:left.find('/')]
year = left[left.find('/')+1:]
print('Día: {d}; mes: {m}; año: {y}.'.format(d=day, m=month, y=year))
