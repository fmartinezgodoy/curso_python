badge = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
selected = input("Ingrese una divisa: ").capitalize()

print(badge.get(selected) if selected in badge else "No está disponible")
