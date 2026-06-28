FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip py3-serial

RUN pip install paho-mqtt

COPY resol_mqtt.py /app/resol_mqtt.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
