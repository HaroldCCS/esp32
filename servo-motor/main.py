from machine import Pin, PWM, Timer
import wifi
import mqttClient

servo=PWM(Pin(33), freq=50)
temporiza=Timer(0)


#----------------------------------------------------servo motor ---------------------------------------
def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
    print(valor_mapeado)
    return valor_mapeado


def main(topic, msg):
    try:
        fun=int (msg.decode())
        angulo = float(fun)
        if angulo >= 0 and angulo <= 180:
            servo.duty(int (mapear (angulo, 0,180,24,127)))
            print("angulo", angulo)
        else:
            print("Digite un angulo entre 0 y 180")
    except:
        print("Error con el dato obtenido")
#----------------------------------------------------servo motor ---------------------------------------

wifi.Wifi()
client = mqttClient.MqttClient(main)
while True:
    print ("esperando")
    client.client.wait_msg()