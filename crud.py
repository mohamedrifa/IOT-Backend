from database import SessionLocal
from models import RawData, Alert
from thresholds import THRESHOLDS
import json

def save_sensor_data(topic, data):
    db = SessionLocal()
    row = RawData(topic=topic, **data)
    db.add(row)
    db.commit()
    db.close()

def check_alerts(topic, data):
    violated = {}
    for key, value in data.items():
        low, high = THRESHOLDS[key]
        if value < low or value > high:
            violated[key] = value

    if violated:
        db = SessionLocal()
        alert = Alert(
            topic=topic,
            violated_keys=",".join(violated.keys()),
            values=json.dumps(violated)
        )
        db.add(alert)
        db.commit()
        db.close()
