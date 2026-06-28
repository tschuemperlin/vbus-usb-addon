FROM ghcr.io/home-assistant/aarch64-base:latest

# Debian-Pakete installieren
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-serial && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Python-Abhängigkeiten
RUN pip3 install --no-cache-dir paho-mqtt

# Dateien ins Image kopieren
COPY resol_mqtt.py /app/resol_mqtt.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
