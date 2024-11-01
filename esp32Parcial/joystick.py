
from machine import Pin, SoftI2C, ADC
class Joystick:
    def __init__(self, pin_x, pin_y, boton):
        self.x = ADC(Pin(pin_x))  # Eje X del joystick
        self.y = ADC(Pin(pin_y))  # Eje Y del joystick
        self.x.atten(ADC.ATTN_11DB)
        self.y.atten(ADC.ATTN_11DB)
        self.boton = Pin(boton, Pin.IN, Pin.PULL_UP)

    
    def detectar_direccion_x(self):
        mitad = 2048

        valorx = self.x.read()
        response_x = "none" #'izq' 'none' 'der'

        if (valorx > 3000):
            response_x = 'der'

        if (valorx < 1000):
            response_x = 'izq'

        return response_x

        
    def boton_oprimido(self):
        return not self.boton.value()