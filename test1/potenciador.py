from machine import Pin, ADC, I2C
from utime import sleep_ms



adc = ADC(Pin(32))

adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

while True:
    sleep_ms(100)
    print(adc.read())