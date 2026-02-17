from fastapi import FastAPI
from threading import Thread
from mqtt_client import start_mqtt
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start():
    Thread(target=start_mqtt, daemon=True).start()

@app.get("/")
def root():
    return {"status": "API running"}
