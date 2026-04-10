from datetime import datetime

class RegistroHistorico:
    def __init__(self, usuario_atual: str, usuario_anterior: str):
        self.usuario_atual = usuario_atual
        self.usuario_anterior = usuario_anterior
        self.data_transferencia = datetime.now().isoformat()

    def to_dict(self):
        return {
            "usuario_atual": self.usuario_atual,
            "usuario_anterior": self.usuario_anterior,
            "data_transferencia": self.data_transferencia
        }
