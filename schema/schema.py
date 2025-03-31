from pydantic import BaseModel

class AgenteBasico(BaseModel):
    prompt: str
    user_id: int