from database import engine, Base
from models import RawData, Alert

Base.metadata.create_all(bind=engine)

print("✅ Tables created")
