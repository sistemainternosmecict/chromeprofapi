from .termo import Termo


class Devolucao(Termo):
    def __init__(self, dispositivo, responsavel, cpf, matricula, telefone, unidade, data_devolucao: str, estado_aparelho: str, observacoes: str):
        super().__init__(dispositivo, responsavel, cpf, matricula, telefone, unidade)
        self.data_devolucao = data_devolucao
        self.estado_aparelho = estado_aparelho
        self.observacoes = observacoes

    def gerar_termo(self) -> str:
        return f"""
        TERMO DE DEVOLUÇÃO

        Dispositivo: {self.dispositivo.serial}
        Responsável: {self.responsavel}
        Unidade: {self.unidade}
        Data: {self.data_devolucao}

        Estado: {self.estado_aparelho}
        Observações: {self.observacoes}
        """

    def obter_termo(self):
        data = super().obter_termo()
        data.update({
            "data_devolucao": self.data_devolucao,
            "estado_aparelho": self.estado_aparelho,
            "observacoes": self.observacoes,
            "tipo": "devolucao"
        })
        return data
