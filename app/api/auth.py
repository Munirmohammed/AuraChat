from fastapi import APIRouter
from app.auth.jwt import create_jwt

router = APIRouter()

@router.post('/login')
def login(username: str):
    return {'token': create_jwt(username)}