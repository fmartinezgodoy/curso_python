import os
import time
from pynput.mouse import Button, Controller

########################################################################################################################

mouse = Controller()

########################################################################################################################

def bot(p11, p12, p13, p14, p21, p22, p23, p24,  delay, repeticiones):

    for i in range(5):
        print("Inicializando bot en {}...".format(5 - i))
        time.sleep(1)
    repeticion = 0

    while True:
        # bloque 1
        mouse.position = (p11)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(delay)

        #bloque 2
        mouse.position = (p12)
        time.sleep(0.1)

        #bloque 3
        mouse.position = (p13)
        time.sleep(0.1)

        #bloque 4
        mouse.position = (p14)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)

        ############## ETAPA 2

        mouse.position = (p21)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(delay)

        # bloque 2
        mouse.position = (p22)
        time.sleep(0.1)

        # bloque 3
        mouse.position = (p23)
        time.sleep(0.1)

        # bloque 4
        mouse.position = (p24)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)

        if repeticion == repeticiones:
            break

        repeticion += 1


def main():
    p11 = (218, 620)
    p12 = (317, 1021)
    p13 = (504, 1022)
    p14 = (518, 864)

    p21 = (189, 554)
    p22 = (284, 1024)
    p23 = (515, 1023)
    p24 = (480, 925)

    delay = float(input("Delay: "))
    reps = int(input("Repeticiones: "))

    print("\nInicializando bot... \n")

    bot(p11, p12 ,p13 ,p14, p21, p22, p23, p24, delay, reps)


########################################################################################################################

print("Inicializando...\n")

while True:
    if input("[y/n]: ") == "y":
        main()
    else:
        print("\nTerminando...")
        break

