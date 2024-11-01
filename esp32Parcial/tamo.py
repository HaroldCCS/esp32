from machine import Pin
from tm1637 import TM1637

class Tm:
    def __init__(self, dio, clk):
        self.tm = TM1637(clk=Pin(clk), dio=Pin(dio))
        self.score = 0

    def show(self, score):
        self.score = self.score + score
        self.tm.show(str(self.score))