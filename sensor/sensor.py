import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause
from time import sleep

switch = Button(4)
rf = Button(26)

# This is the Publisher
def switchpress():
    client.publish("home-assistant/livesafe/switch", "switch off!")
    print("switch")


def rfpress():
    client.publish("home-assistant/livesafe/switch", "rf broken!")
    print("rf")


client = mqtt.Client()
client.connect("192.168.8.234", 1883, 60)

switch.when_activated = switchpress
rf.when_activated = rfpress

# Does the exact same as two lines above
# switch.when_pressed = switchpress
# rf.when_pressed = rfpress

pause()

client.disconnect()
