from fastapi import FastAPI, WebSocket
from app.websockets.manager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()

@app.get('/')
def read_root():
    return {'message': 'AuraChat WebSocket Engine'}