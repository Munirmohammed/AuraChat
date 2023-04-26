import time

def create_jwt(user_id: str):
    return f'{user_id}.signature.{time.time()}'