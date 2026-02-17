from database import SessionLocal
from models import RawData, Alert
from datetime import datetime
import random

db = SessionLocal()

topics = ["factory/temp", "factory/humidity", "factory/voltage"]

for i in range(30):
    raw = RawData(
        topic=random.choice(topics),
        temperature=round(random.uniform(20, 45), 2),
        humidity=round(random.uniform(30, 85), 2),
        voltage=round(random.uniform(210, 250), 2),
        current=round(random.uniform(0.5, 6.0), 2),
        pressure=round(random.uniform(900, 1100), 2),
        timestamp=datetime.utcnow()
    )
    db.add(raw)

    # randomly create alerts
    if random.choice([True, False]):
        alert = Alert(
            topic=raw.topic,
            violated_keys="temperature,voltage",
            values=f"{raw.temperature},{raw.voltage}",
            timestamp=datetime.utcnow()
        )
        db.add(alert)

db.commit()
db.close()

print("✅ 30 RawData + random Alerts inserted")
