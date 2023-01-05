# Imports go at the top
from microbit import *

rojo = pin0
azul = pin1
verde = pin2
t = 1000

display.scroll("start", delay=230)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("off", delay=80)
        azul.write_digital(0)
        break;
    elif button_a.is_pressed():
         #ROJO
        azul.write_digital(0)
        rojo.write_digital(1)
        sleep(t)
        rojo.write_digital(0)
    elif button_b.is_pressed():
        #AZUL
        azul.write_digital(0)
        verde.write_digital(1)
        sleep(t)
        verde.write_digital(0)
    else:
        azul.write_digital(1)
