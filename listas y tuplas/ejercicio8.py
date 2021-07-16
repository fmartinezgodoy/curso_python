charList = list(
    input("Ingrese una palabra: ")
)

check = True

for i in range(
    round(
        float(
            len(charList)/2
        )
    )
):
    if charList[i] != charList[len(charList)-1-i]:
        check = False
        break


print("La palabra ingresada {}es un palíndromo.".format("" if check else "no "))
