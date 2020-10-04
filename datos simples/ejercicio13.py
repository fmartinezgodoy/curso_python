


interes = 0.04


cantidad = float(input("Igrese cantidad depositada: "))

for i in range(3):
    ahorros = round(cantidad*(1+interes)**(i+1),2)
    print ("La cantidad de ahorros en el año " + str(i+1) + " es: " + str(ahorros))

