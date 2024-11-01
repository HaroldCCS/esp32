from machine import Pin
import time
import random

import nave
import oled
import disparo
import tamo


BOTON_ROJO = Pin(23, Pin.OUT)

instance_oled = oled.Oled()
ooled = instance_oled.obtener_oled()




def main():
    contador = 0
    instancia_nave = nave.Nave(5)
    instancia_nave.joystick(34,35,32)
    instancia_tm = tamo.Tm(26,27)
    instancias_disparos = []

    while (True):
        ooled.fill(0)
        #generar disparo hacia abajo
        contador = contador + 1
        if (contador == 4):
            contador = 0
            nuevo_disparo = disparo.Disparo(random.randint(0, 127),0,random.randint(2,4),'abajo', random.randint(5,20), random.randint(4,10))
            instancias_disparos.append(nuevo_disparo)


        #mover nave
        instancia_nave.mover()
        instancia_nave.pintar(ooled)

        #disparar
        nuevo_disparo = instancia_nave.validar_disparo()
        if (nuevo_disparo):
            instancias_disparos.append(nuevo_disparo)

        #mover disparos
        for o in instancias_disparos[:]: 
            eliminar = o.pintar(ooled)
            if eliminar:
                instancias_disparos.remove(o)
                continue

        #buscar colisiones
        salir = False
        for o in instancias_disparos[:]: 
            if (o.hay_colision(instancia_nave)):
                salir = True
                break

            for i in instancias_disparos[:]:
                if (i == o):
                    continue
                if (o.hay_colision(i)):
                    instancia_tm.show(100)
                    instancias_disparos.remove(i)
                    instancias_disparos.remove(o)
                    break

        if salir:
            break
        
        
                
        ooled.text(str(len(instancias_disparos)),0,0,1)
        time.sleep(0.1)
        ooled.show()


while (True):
    main()

    ooled.fill(0)
    ooled.text("has perdido",0,0,1)
    ooled.show()

    time.sleep(3)

    # while (True):
    #     if (BOTON_ROJO.value() == 1):
    #         break

