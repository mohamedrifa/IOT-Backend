from fastapi import APIRouter
from database import SessionLocal
from models import RawData, Alert

router = APIRouter()

@router.get("/stats")
def get_stats():
    db = SessionLocal()
    total = db.query(RawData).count()
    latest = db.query(RawData).order_by(RawData.id.desc()).first()
    active_alerts = db.query(Alert).order_by(Alert.id.desc()).limit(5).all()
    return {
        "total": total,
        "latest": latest,
        "alerts": active_alerts
    }

@router.get("/raw")
def get_raw():
    db = SessionLocal()
    return db.query(RawData).order_by(RawData.id.desc()).limit(50).all()

@router.get("/alerts")
def get_alerts():
    db = SessionLocal()
    return db.query(Alert).order_by(Alert.id.desc()).all()
