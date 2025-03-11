import websocket
import json
import paho.mqtt.client as mqtt

# Configuración de conexión
WS_URL = "ws://192.168.4.69:7891"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "switchbee/status"

def on_message(ws, message):
    try:
        data = json.loads(message)
        if "id" in data and "newValue" in data:
            payload = {
                "id": data["id"],
                "status": "Encendido" if data["newValue"] == 100 else "Apagado"
            }
            client.publish(MQTT_TOPIC, json.dumps(payload))
    except Exception as e:
        print(f"Error procesando mensaje: {e}")

ws = websocket.WebSocketApp(WS_URL, on_message=on_message)

# Cliente MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# Iniciar WebSocket
ws.run_forever()
