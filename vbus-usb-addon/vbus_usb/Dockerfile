FROM python:3.11-slim
RUN pip install paho-mqtt
COPY resol_mqtt.py /app/resol_mqtt.py
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh
CMD ["/app/run.sh"]
