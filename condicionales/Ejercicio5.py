userAge = float(input("Ingrese su edad: "))

userIncome = float(input("Ingrese su salario: "))

if userAge >= 16 and userIncome >= 1000:
    print("El usuario tiene que tributar.")
else:
    print("El usuario no tiene que tributar.")
