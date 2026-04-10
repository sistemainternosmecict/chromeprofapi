from typing import Dict
from src.classes.dispositivo import Dispositivo


class DispositivoRepository:
    def __init__(self):
        self.db: Dict[str, Dispositivo] = {}

    def adicionar(self, dispositivo: Dispositivo):
        self.db[dispositivo.serial] = dispositivo

    def buscar(self, serial: str):
        return self.db.get(serial)

    def listar(self):
        return list(self.db.values())
