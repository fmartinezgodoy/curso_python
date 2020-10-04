import math
import random
import pynput
import time
from pynput.mouse import Button, Controller
from threading import Timer
from pynput import keyboard


mouse = Controller()

#parametros
param_vel_base = 55
param_vel_inc = 5
param_vel_max = param_vel_base + param_vel_inc
param_resolution_x = 1920
param_resolution_y = 1080
param_center_x = int(round(param_resolution_x / 2))
param_center_y = int(round(param_resolution_y / 2))
param_rad = 300
param_vel_spin = 0.001


def velocidad_giro(base, inc):
    return round(random.random() * inc + base)


count = 0
contador_vueltas = 0

time.sleep(5)

mouse.press(Button.left)

while True:

    while count < (360 - param_vel_max):

        count += velocidad_giro(param_vel_base, param_vel_inc)

        pos_x =int(param_center_x + param_rad * math.cos(math.radians(count)))
        pos_y =int(param_center_y + param_rad * math.sin(math.radians(count)))
        print(count)
        mouse.position=(pos_x, pos_y)
        time.sleep(param_vel_spin)
    count = 0
    contador_vueltas += 1

