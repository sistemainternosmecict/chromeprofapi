from .termo import Termo


class Aquisicao(Termo):
    def __init__(self, dispositivo, responsavel, cpf, matricula, telefone, unidade, data_aquisicao: str, observacoes: str):
        super().__init__(dispositivo, responsavel, cpf, matricula, telefone, unidade)
        self.data_aquisicao = data_aquisicao
        self.observacoes = observacoes

    def gerar_termo(self) -> str:
        return f"""
        TERMO DE AQUISIÇÃO

        Dispositivo: {self.dispositivo.serial}
        Responsável: {self.responsavel}
        Unidade: {self.unidade}
        Data: {self.data_aquisicao}

        Observações: {self.observacoes}
        """

    def obter_termo(self):
        data = super().obter_termo()
        data.update({
            "data_aquisicao": self.data_aquisicao,
            "observacoes": self.observacoes,
            "tipo": "aquisicao"
        })
        return data
