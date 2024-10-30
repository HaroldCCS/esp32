from machine import Pin
from utime import sleep


class SecuenciaCarro: 
    cantidad_leds = 0
    cantidad_mitad_leds = 0
    pines_leds = []

    def __init__(self, pines_leds):
        self.pines_leds = pines_leds
        self.cantidad_leds = len(pines_leds)
        self.cantidad_mitad_leds = int(self.cantidad_leds / 2)


    #--------------------------- Funciones generales ----------------------------
    def ejecutarLeds(self, leds, estado, esperar = 0):
        for i in leds:
            i.value(estado)
        sleep(esperar)

    def apagarLeds(self, leds, esperar = 0):
        self.ejecutarLeds(leds, 0, esperar)

    def encenderLeds(self, leds, esperar = 0):
        self.ejecutarLeds(leds, 1, esperar)

    def encenderApagarVariosLedsAlMismoTiempo(self, leds, cantidad_parpadeo = 1):
        for i in range(cantidad_parpadeo):
            esperar = 0.1
            self.encenderLeds(leds, esperar)
            self.apagarLeds(leds, esperar)
    #--------------------------- Funciones generales ----------------------------


    #--------------------------- Secuencias carro ----------------------------
    #Parte 1 secuencia carro
    def unLedEnLinea(self, leds):
        for i in leds:
            i.value(1)
            sleep(0.1)
            i.value(0)

    #Parte 2 secuencia carro
    def variosLedsEnLinea(self, leds): 
        #fase 0 apagado
        #fase 1 apagado consecutivo
        #fase 2 apagado consecutivo 
        #fase 3 encendido concecutivo

        leds_estado = []
        def runEstados(leds_estado):
            sleep(0.15)
            for o in leds_estado:
                if (o[1] == 0):
                    o[1] = 1
                elif (o[1] == 1 ):
                    o[1] = 2
                elif (o[1] == 2):
                    o[1] = 3
                    o[0].value(1)
                elif (o[1] == 3):
                    o[1] = 0
                    o[0].value(0)
                leds_estado[0][0].value(1)

        for i in leds:
            leds_estado.append([i, 1])
            runEstados(leds_estado)

        size = len(leds) * 2
        while size: 
            size = size - 1
            runEstados(leds_estado)

    #Parte 3 secuencia carro
    def encenderMitadPorMitad(self, leds):
        #Primera mitad de la linea de leds
        self.encenderApagarVariosLedsAlMismoTiempo(leds[:self.cantidad_mitad_leds], 3)

        #Segunda mitad de la linea de leds
        self.encenderApagarVariosLedsAlMismoTiempo(leds[self.cantidad_mitad_leds:], 3)

    #Parte 4 secuenta carro
    def encenderLedsParalelos(self, leds, cantidad_repeticiones = 1, adentro_hacia_afuera = False):
        rango = range(self.cantidad_mitad_leds)

        if (adentro_hacia_afuera):
            rango = reversed(rango)

        for o in range(cantidad_repeticiones):
            for i in rango:
                temp_leds = []
                temp_leds.append(leds[i])
                temp_leds.append(leds[self.cantidad_leds - i - 1])
                self.encenderApagarVariosLedsAlMismoTiempo(temp_leds, 3)
            self.encenderApagarVariosLedsAlMismoTiempo(leds, 3)

    #Parte 5 secuenta carro
    def encender_todos_adentro_hacia_afuera(self, leds, cantidad_repeticiones = 1, afuera_hacia_dentro = False):
        esperar = 0.1
        for i in range(cantidad_repeticiones):
            for i in reversed(range(self.cantidad_mitad_leds)):
                temp_leds = []
                temp_leds.append(leds[i])
                temp_leds.append(leds[self.cantidad_leds - i - 1])
                self.encenderLeds(temp_leds, esperar)
            
            for i in (range(self.cantidad_mitad_leds)):
                temp_leds = []
                temp_leds.append(leds[i])
                temp_leds.append(leds[self.cantidad_leds - i - 1])
                self.apagarLeds(temp_leds, esperar)

    #Parte 6 secuenta carro
    def encender_parcial_adentro_hacia_afuera(self, leds, cantidad_repeticiones = 1, afuera_hacia_dentro = False):
        esperar = 0.05
        for i in range(cantidad_repeticiones):
            for i in reversed(range(self.cantidad_mitad_leds)):
                temp_leds = []
                temp_leds.append(leds[i])
                temp_leds.append(leds[self.cantidad_leds - i - 1])
                self.encenderApagarVariosLedsAlMismoTiempo(temp_leds, esperar)
            
            for i in (range(self.cantidad_mitad_leds)):
                temp_leds = []
                temp_leds.append(leds[i])
                temp_leds.append(leds[self.cantidad_leds - i - 1])
                self.encenderApagarVariosLedsAlMismoTiempo(temp_leds, esperar)
    #--------------------------- Secuencias carro ----------------------------


    def run(self,cantidad_repeticiones, un_led_en_linea = True, varios_leds_en_linea = True, mitad_por_mitad = True, leds_paralelos = True, todos_adentro_hacia_afuera = True, parcial_adentro_hacia_afuera = True):
        leds = []
        
        for i in pines_leds:
            leds.append(Pin(i, Pin.OUT))

        self.apagarLeds(leds)
        
        while True: 

            if (un_led_en_linea):
                temp_cantidad = cantidad_repeticiones
                while temp_cantidad:
                    temp_cantidad = temp_cantidad - 1
                    self.unLedEnLinea(leds)
                    self.unLedEnLinea(leds[::-1])
                    self.apagarLeds(leds)

            if (varios_leds_en_linea):
                temp_cantidad = cantidad_repeticiones
                while temp_cantidad:
                    temp_cantidad = temp_cantidad - 1

                    self.variosLedsEnLinea(leds)
                    self.apagarLeds(leds)

                    self.variosLedsEnLinea(leds[::-1])
                    self.apagarLeds(leds)

            if (mitad_por_mitad):
                temp_cantidad = cantidad_repeticiones
                while temp_cantidad:
                    temp_cantidad = temp_cantidad - 1
                    self.encenderMitadPorMitad(leds)
                    self.apagarLeds(leds)

            if (leds_paralelos):
                self.encenderLedsParalelos(leds, cantidad_repeticiones)
                sleep(0.1)
                self.apagarLeds(leds)
                self.encenderLedsParalelos(leds, cantidad_repeticiones, True)
                self.apagarLeds(leds)


            if (todos_adentro_hacia_afuera): 
                self.encender_todos_adentro_hacia_afuera(leds, cantidad_repeticiones)
                self.apagarLeds(leds)
            
            if (parcial_adentro_hacia_afuera): 
                self.encender_parcial_adentro_hacia_afuera(leds,cantidad_repeticiones)
                self.apagarLeds(leds)

            self.encenderApagarVariosLedsAlMismoTiempo(leds, 3)



pines_leds = [5,4,27,26,18,19,21,12]

carro = SecuenciaCarro(pines_leds)
carro.run(2)