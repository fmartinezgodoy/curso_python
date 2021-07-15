quit = False

while not quit:
    prompt = input("Ingrese algo: ")
    if (prompt == 'salir'):
        quit = True
    else:
        print(prompt)
