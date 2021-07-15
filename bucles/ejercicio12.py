phrase = input("Ingrese una frase: ")
sample = input("Ingrese una letra: ")

count = 0

for char in phrase:
    if char == sample:
        count += 1

print(
    "La letra '{}' aprece {} veces en la frase.".format(
        sample, count)
    )
