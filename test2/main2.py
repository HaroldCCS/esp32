from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C


#oled
i2c = I2C(0, scl=Pin(22), sda=Pin(23))
oled_width = 128
oled_height = 64
devices = i2c.scan()
print(devices)
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.text("hola",0,0,1)
oled.show()

