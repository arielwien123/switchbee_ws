FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install websocket-client paho-mqtt

CMD ["python", "switchbee_ws.py"]
