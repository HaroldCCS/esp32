from machine import Pin
from utime import sleep





led2 = Pin(5, Pin.OUT)
boton = Pin(18, Pin.OUT)
last_state = 0
while True:
    sleep(0.2)
    if (boton.value() == 1):
        if ( last_state == 0):
            print("on")
            last_state = 1
        led2.value(1)
    else:
        if ( last_state == 1):
            print("off")
            last_state = 0
        led2.value(0)
