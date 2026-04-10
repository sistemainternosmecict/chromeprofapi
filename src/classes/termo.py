class Termo:
    def __init__(self, dispositivo, responsavel: str, cpf: str, matricula: str, telefone: str, unidade: str):
        self.dispositivo = dispositivo
        self.responsavel = responsavel
        self.cpf = cpf
        self.matricula = matricula
        self.telefone = telefone
        self.unidade = unidade

    def gerar_termo(self) -> str:
        raise NotImplementedError

    def obter_termo(self) -> dict:
        return {
            "serial": self.dispositivo.serial,
            "responsavel": self.responsavel,
            "cpf": self.cpf,
            "matricula": self.matricula,
            "telefone": self.telefone,
            "unidade": self.unidade
        }
