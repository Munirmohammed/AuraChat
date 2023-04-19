from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    id: int
    sender: str
    content: str
    timestamp: datetime