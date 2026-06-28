#!/usr/bin/env python3
import os
import time
import paho.mqtt.client as mqtt
from vbus import VBusReader  # oder aus deiner bisherigen Bibliothek

MQTT_HOST = os.getenv("MQTT_HOST", "homeassistant")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER", "")
MQTT_PASS = os.getenv("MQTT_PASS", "")
MQTT_TOPIC = "resol/midi_pro/"

DEVICE = "/dev/ttyUSB0"
BAUD = 9600

def publish(client, key, value):
    client.publish(MQTT_TOPIC + key, value, retain=True)

def main():
    client = mqtt.Client()
    if MQTT_USER:
        client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    reader = VBusReader(DEVICE, BAUD)

    while True:
        frame = reader.read_frame()
        if frame:
            publish(client, "raw", frame)
        time.sleep(1)

if __name__ == "__main__":
    main()
