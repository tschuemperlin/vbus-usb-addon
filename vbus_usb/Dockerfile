FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install paho-mqtt pyserial resol-vbus

COPY resol_mqtt.py /app/resol_mqtt.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
