from machine import Pin
from umqtt.simple import MQTTClient
import time

class MqttClient :
    def __init__(self, callback):
      MQTT_CLIENT_ID = "estacion-incendio-harold141"
      MQTT_BROKER    = "broker.hivemq.com"
      MQTT_USER      = ""
      MQTT_PASSWORD  = ""
      MQTT_TOPIC      = "lobodinamita/bum"

      led = Pin(2, Pin.OUT)
      led.value(0)
      def connect(): 
        print("Connecting to MQTT server... ", end="")
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
        client.set_callback(callback)
        client.connect()
        client.subscribe(MQTT_TOPIC)
        print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, MQTT_TOPIC))
        led.value(1)
        return client

      while True:
        try:
          self.client = connect()
          break
        except:
          print("Connection failed, retrying in 5 seconds...")
          time.sleep(5)
