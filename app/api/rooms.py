from fastapi import APIRouter

router = APIRouter()

@router.get('/rooms')
def list_rooms():
    return ['general', 'random', 'development']