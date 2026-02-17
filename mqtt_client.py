import json
import os
import paho.mqtt.client as mqtt
from crud import save_sensor_data, check_alerts
from dotenv import load_dotenv

load_dotenv()

BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", None)
MQTT_PASS = os.getenv("MQTT_PASS", None)

TOPICS = [
    "factory/temp",
    "factory/humidity",
    "factory/voltage",
    "factory/current",
    "factory/pressure"
]

def start_mqtt():
    client = mqtt.Client()

    # If credentials exist, set them
    if MQTT_USER and MQTT_PASS:
        client.username_pw_set(MQTT_USER, MQTT_PASS)

    def on_connect(client, userdata, flags, rc):
        print("MQTT Connected with code", rc)
        for topic in TOPICS:
            client.subscribe(topic)
            print("Subscribed to", topic)

    def on_message(client, userdata, msg):
        try:
            payload = msg.payload.decode()
            print("RAW:", payload)
            data = json.loads(payload)
            print("PARSED:", data)
            save_sensor_data(msg.topic, data)
            check_alerts(msg.topic, data)
        except Exception as e:
            print("Bad message ignored:", e)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_forever()
