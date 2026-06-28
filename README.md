# VBus USB Reader Add-on

Dieses Add-on liest Resol VBus Daten (Midi Pro) über USB (`/dev/ttyUSB0`)
und veröffentlicht sie via MQTT für Home Assistant.

## Konfiguration

- `device`: Pfad zum USB-Gerät (Standard: `/dev/ttyUSB0`)
- `baudrate`: Baudrate (Standard: `9600`)
- `mqtt_host`: MQTT Broker Host (Standard: `homeassistant`)
- `mqtt_port`: MQTT Broker Port (Standard: `1883`)
- `mqtt_user`: MQTT Broker User (Standard: ``)
- `mqtt_pass`: MQTT Broker Pass (Standard: ``)

## MQTT Topics

Die Daten werden unter `resol/midi_pro/` veröffentlicht, z. B.:

- `resol/midi_pro/temp_1`
- `resol/midi_pro/temp_2`
- `resol/midi_pro/speed_1`
- `resol/midi_pro/irradiation`
- `resol/midi_pro/relay_1`
