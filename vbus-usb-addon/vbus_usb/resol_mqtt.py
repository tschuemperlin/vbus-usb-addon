#!/usr/bin/env python3
import time
import serial
import paho.mqtt.client as mqtt

MQTT_HOST = "homeassistant"
MQTT_PORT = 1883
MQTT_TOPIC = "resol/midi_pro/raw"

DEVICE = "/dev/ttyUSB0"
BAUD = 9600

def main():
    print("Starting VBus USB Reader (raw)…")

    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, 60)

    ser = serial.Serial(DEVICE, BAUD, timeout=1)

    while True:
        data = ser.read(64)
        if data:
            hex_str = data.hex()
            client.publish(MQTT_TOPIC, hex_str, retain=False)
            print(hex_str)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
