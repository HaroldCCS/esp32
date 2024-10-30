from machine import Pin
from umqtt.simple import MQTTClient
import time

class MqttClient :
    def __init__(self):
      MQTT_CLIENT_ID = "pepepeppepepe"
      MQTT_BROKER    = "9567cff38db0448eba7dc78f411a64cf.s1.eu.hivemq.cloud:8883"
      MQTT_USER      = "test"
      MQTT_PASSWORD  = "test"
      MQTT_TOPIC      = "alarma/piso-3"

      led = Pin(2, Pin.OUT)
      led.value(0)
      def connect(): 
        print("Connecting to MQTT server... ", end="")
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
        client.connect()
        led.value(1)
        return client

      while True:
        try:
          self.client = connect()
          break
        except:
          print("Connection failed, retrying in 5 seconds...")
          time.sleep(5)

    def publish(self, msg):
        self.client.publish("alarma/piso-3", msg)
