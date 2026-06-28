FROM ghcr.io/home-assistant/aarch64-addon-base-python3:latest

# Python-Abhängigkeiten installieren
RUN pip3 install --no-cache-dir paho-mqtt

COPY resol_mqtt.py /app/resol_mqtt.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
