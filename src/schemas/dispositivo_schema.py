from pydantic import BaseModel

class DispositivoCreate(BaseModel):
    serial: str
    modelo: str
    status: str
