from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI(
    title="DevOps Platform API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the DevOps Platform API",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname()
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname()
    }
