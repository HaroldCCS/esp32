from utime import sleep_ms
from tm1637 import TM1637
from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import framebuf


#tm
tm = TM1637(clk=Pin(26), dio=Pin(27))


#potenciador
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

adcIzq = ADC(Pin(33))
adcIzq.atten(ADC.ATTN_11DB)
adcIzq.width(ADC.WIDTH_12BIT)


#oled
i2c = I2C(0, scl=Pin(23), sda=Pin(22))
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
fb = oled.framebuf


#joystick
x = ADC(Pin(35))
y = ADC(Pin(34))
boton = Pin(25, Pin.IN, Pin.PULL_UP)

x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

mitad = 2048



last_adc = 'izq'
while True:
    print(boton.value())
    #Oled y Joystick
    valorx = x.read()
    valory = y.read()

    oled.fill(0)

    if (valorx > 3000):
        last_adc = 'der'

    if (valorx < 1000):
        last_adc = 'izq'

    porcentaje = 0
    if (last_adc == 'izq'):
        porcentaje = int(( adcIzq.read() / 4095) * 100)
    else:
        porcentaje = int(( adc.read() / 4095) * 100)

    tm.show(str(porcentaje))
    oled.show()

    sleep_ms(10)
