import time
from pynput.mouse import Button, Controller

mouse = Controller()

for i in range(5):
    print("Tomando posición en {}...".format(5-i))
    time.sleep(1)

while True:
    print(mouse.position)
    check = input("Nuevas coordenadas? y/n: ")
    if check == "y":
        for i in range(5):
            print("Tomando posición en {}...".format(5-i))
            time.sleep(1)
    elif check == "n":
        break