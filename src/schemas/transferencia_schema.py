from pydantic import BaseModel

class TransferenciaCreate(BaseModel):
    serial: str
    novo_usuario: str
