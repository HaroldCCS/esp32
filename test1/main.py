from machine import Pin, ADC, I2C
from utime import sleep_ms
from tm1637 import TM1637
from ssd1306 import SSD1306_I2C

#tm
tm = TM1637(clk=Pin(27), dio=Pin(26))


#potenciador
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

#oled
i2c = I2C(0, scl=Pin(23), sda=Pin(22), freq=100000)
oled_width = 128
oled_height = 64
devices = i2c.scan()
print(devices)
oled = SSD1306_I2C(oled_width, oled_height, i2c)



while True:
    if (adc.read() > 2040):
        oled.text("derecha")
    else:
        oled.text("izquierda")
    oled.show()
    tm.show(str(adc.read()))
    sleep_ms(1000)

