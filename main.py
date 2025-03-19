from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

class AgenteBasico(BaseModel):
    prompt: str
        

@app.post("/agente-basico")
async def agente_basico(prompt: AgenteBasico):
    return {"prompt": prompt}