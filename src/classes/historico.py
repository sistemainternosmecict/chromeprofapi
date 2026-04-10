from typing import List
from .registro_historico import RegistroHistorico


class Historico:
    def __init__(self):
        self.historico: List[RegistroHistorico] = []

    def carregar_historico(self, dados: list):
        for item in dados:
            registro = RegistroHistorico(
                item["usuario_atual"],
                item["usuario_anterior"]
            )
            registro.data_transferencia = item["data_transferencia"]
            self.historico.append(registro)

    def inserir_registro(self, registro: RegistroHistorico):
        self.historico.append(registro)

    def obter_ultimo_registro(self):
        if not self.historico:
            return None
        return self.historico[-1]

    def limpar_historico_do_aparelho(self):
        self.historico.clear()

    def to_list(self):
        return [r.to_dict() for r in self.historico]
