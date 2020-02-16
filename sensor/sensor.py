import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause
from time import sleep

switch = Button(4)
rf = Button(26)
button = Button(16)
def switchpress():
    client.publish("livesafe/switch", "on")
    print("switch on")


def switchrelease():
    client.publish("livesafe/switch", "off")
    print("switch off")


def rfpress():
    client.publish("livesafe/door", "open")
    print("rf open")


def rfrelease():
    client.publish("livesafe/door", "closed")
    print("rf closed")

def switchrelease():
    client.publish("livesafe/switch", "off")
    print("switch off")


def buttonpress():
    client.publish("livesafe/button", "pressed")
    print("button pressed")


def buttonrelease():
    client.publish("livesafe/button", "released")
    print("button released")

client = mqtt.Client()
client.connect("192.168.8.234", 1883, 60)

switch.when_activated = switchpress
switch.when_deactivated = switchrelease
rf.when_activated = rfpress
rf.when_deactivated = rfrelease
button.when_activated = buttonpress
button.when_deactivated = buttonrelease

pause()

client.disconnect()
