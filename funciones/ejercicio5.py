import math

def area(radio):
    return (2 * math.pi * radio**2)

def volumen(area, altura):
    return round(area * altura)

print(volumen(area(5), 10))
