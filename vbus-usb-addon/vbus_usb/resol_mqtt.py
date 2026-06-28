#!/usr/bin/env python3
import time
import os
import paho.mqtt.client as mqtt
from resol_vbus import VBusReader  # falls dein Modul anders heisst, hier anpassen

MQTT_TOPIC_BASE = "resol/midi_pro/"

DEVICE = os.getenv("DEVICE", "/dev/ttyUSB0")
BAUD = int(os.getenv("BAUDRATE", "9600"))
MQTT_HOST = os.getenv("MQTT_HOST", "homeassistant")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

def publish(client, key, value):
    topic = MQTT_TOPIC_BASE + key
    client.publish(topic, value, retain=True)

def main():
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    reader = VBusReader(DEVICE, BAUD)

    while True:
        frame = reader.read_frame()

        # Hier musst du deine konkreten Datenpunkte aus dem Resol Midi Pro mappen
        # Beispielhaft:
        data = reader.parse_frame(frame)

        # Diese Keys musst du an deine reale Struktur anpassen
        publish(client, "temp_1", data.get("temp_1"))
        publish(client, "temp_2", data.get("temp_2"))
        publish(client, "speed_1", data.get("speed_1"))
        publish(client, "irradiation", data.get("irradiation"))
        publish(client, "relay_1", data.get("relay_1"))

        time.sleep(5)

if __name__ == "__main__":
    main()
