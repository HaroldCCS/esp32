class Disparo:
    def __init__(self, x, y, mover_pixeles, direccion, ancho = 2, alto = 4):
        self.mover_pixeles = mover_pixeles
        self.direccion = direccion
        self.x = x
        self.ancho = ancho

        self.y = y
        self.alto = alto
    
    def pintar(self, oled):

        if (self.direccion == 'arriba'):
            self.y = self.y - self.mover_pixeles
            if (self.y < 0):
                return True


        if (self.direccion == 'abajo'):
            self.y = self.y + self.mover_pixeles
            if (self.y > 63):
                return True

        for i in range(self.x, self.x + self.ancho):
            for o in range(self.y, self.y + self.alto):
                oled.pixel(i, o, 1)


    def posicion_en_pantalla(self): 
        return [self.x, self.y, self.ancho, self.alto]

    def hay_colision(self, elemento):
        posiciones_elemento = elemento.posicion_en_pantalla()

        colision_x = (posiciones_elemento[0] + posiciones_elemento[2] < self.x ) or (posiciones_elemento[0] > self.x + self.ancho)
        
        # oled.pixel(0,0, (posiciones_elemento[0] + posiciones_elemento[2] < self.x ))
        # oled.pixel(120,1, (posiciones_elemento[0] > self.x + self.ancho))


        if (colision_x):
            return False
        
        colision_y = (posiciones_elemento[1] + posiciones_elemento[3] < self.y ) or (posiciones_elemento[1] > self.y + self.alto)
        if (colision_y):
            return False

        return True