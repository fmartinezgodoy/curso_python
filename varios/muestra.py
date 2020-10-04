
import random

c = 0

while True:

    num = round(30 * random.random())

    if input("Forzar número") == "y":
        num = input()

    print(num)

