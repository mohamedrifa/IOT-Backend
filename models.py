from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True)
    topic = Column(String(50))
    temperature = Column(Float)
    humidity = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    pressure = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    topic = Column(String(50))
    violated_keys = Column(String(200))
    values = Column(String(200))
    timestamp = Column(DateTime, default=datetime.utcnow)
