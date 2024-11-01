import joystick
import disparo

class Nave:
    def __init__(self, mover_pixeles):
        self.x = 56
        self.ancho = 10

        self.y = 57
        self.alto = 5

        self.mover_pixeles = mover_pixeles


    def joystick(self, pin_x, pin_y, boton): 
        self.instance_joystick = joystick.Joystick(pin_x,pin_y,boton)

    
    def pintar(self, oled):

        #lineas de abajo
        for i in range(self.x, self.x + 10):
            oled.pixel(i, self.y + 4, 1)
            oled.pixel(i, self.y + 3, 1)

        #linea centro
        for i in range(self.x+4, self.x + 6):
            oled.pixel(i, self.y + 2, 1)
            oled.pixel(i, self.y + 1, 1)
            oled.pixel(i, self.y + 0, 1)

    def mover(self):
        lado = self.instance_joystick.detectar_direccion_x()
        if (lado == 'izq' and self.x > 3):
            self.x = self.x - self.mover_pixeles

        if (lado == 'der'and self.x < 127 - 12):
            self.x = self.x + self.mover_pixeles

    def obtener_posiciones_de_disparo(self):
        return [self.x + 4, self.y - 1]

    def validar_disparo(self): 
        if (self.instance_joystick.boton_oprimido()):
            posiciones_disparo = self.obtener_posiciones_de_disparo()

            dis = disparo.Disparo(posiciones_disparo[0],posiciones_disparo[1],4, 'arriba')
            return dis

    def posicion_en_pantalla(self): 
        return [self.x, self.y, self.ancho, self.alto]