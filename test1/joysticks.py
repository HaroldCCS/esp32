from machine import Pin, ADC
from time import sleep
from tm1637 import TM1637


#--------------------------tm
tm = TM1637(clk=Pin(27), dio=Pin(26))

tm.scroll("Harold")
x = ADC(Pin(35))
y = ADC(Pin(34))

x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)

last_x = 2048
last_y = 2048
while True:
    sleep(0.1)

    
    need_print = False
    valorx = x.read()
    if (valorx < 200):
        tm.show("cero")
        continue
    tm.show(str(valorx))

    # if (valorx != last_x):
    #     need_print = True
    #     last_x = valorx

    # valory = y.read()
    # if (valory != last_y):
    #     need_print = True
    #     last_y = valory

    # if (need_print): 
    #     print(valorx, valory)
    #     tm.show(str(valorx))




