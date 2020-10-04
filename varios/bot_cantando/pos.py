import os
import time
from pynput import keyboard
from pynput.mouse import Button, Controller
########################################################################################################################

ruta = "{}\data.txt".format(os.getcwd())
archivo = open(ruta, "r+")

########################################################################################################################

mouse = Controller()

count = 0
stop = 0

pos_1 = []
pos_2 = []
iteración = [0]

########################################################################################################################

def bot(pos_1, pos_2, delay, repeticiones):
    for i in range(5):
        print("Inicializando bot en {}...".format(5 - i))
        time.sleep(1)
    repeticion = 0
    while True:
        # bloque 1
        mouse.position = (pos_1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)
        # bloque 2
        mouse.position = (pos_2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)

        if repeticion == repeticiones:
            break

        repeticion += 1

def main():
    print ("Obteniendo posición...")

    if iteración[0] == 0:

        ruta = "{}\data.txt".format(os.getcwd())
        archivo = open(ruta, "w")

        pos_1 = mouse.position
        archivo.write("{},{},".format(pos_1[0],pos_1[1]))
        print("Primer posición obtenida: {},{}".format(pos_1[0],pos_1[1]))

        archivo.close()
        iteración[0] = 1

    else:

        ruta = "{}\data.txt".format(os.getcwd())
        archivo = open(ruta, "r+")

        pos_2 = mouse.position
        pos = archivo.read()
        print("anterior {}".format(pos))
        pos = ("{},{}".format(pos_2[0],pos_2[1]))
        print("nueva {}".format(pos))
        archivo.write(str(pos))
        #print("Las posiciones obtenidas son {} y {}.".format(pos_1, pos_2))
        archivo.close()
        iteración[0] = 0
    print("")

    check = input("Iniciar? y/n:")

    if check == "y":
        print("")
        repeticiones = int(input("Ingrese cantidad de repeticiones: "))
        delay = float(input("Ingrese delay entre click: "))
        print("")
        print("Iniciando bot")

        ruta = "{}\data.txt".format(os.getcwd())
        archivo = open(ruta, "r+")

        print("SE PICA PADRE")

        pos = archivo.read()
        pos = pos.split(",")

        input()

        ######################################

        posa = [pos[0], pos[1]]
        posb = [pos[2], pos[3]]

        print(pos)

        print("")

        bot(posa, posb, delay, repeticiones)

        print("Finalizando bot...")

        input("Enter para continuar.")

        print("")
    else:
        print("")


    print("")
    print("Esperando posición...")
    print("")

def on_press(key):
    main()

def on_release(key):
    pass


########################################################################################################################

print("Inicializando...")
print("")
print("Esperando confirmación para obtener posición...")

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

