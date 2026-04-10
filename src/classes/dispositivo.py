from .historico import Historico


class Dispositivo:
    STATUS_VALIDOS = {"em uso", "parado", "extraviado", "danificado", "smeict"}

    def __init__(self, serial: str, modelo: str, status: str):
        if status not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido")

        self.serial = serial
        self.modelo = modelo
        self.status = status
        self.historico = Historico()

    def atualizar_status(self, novo_status: str):
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido")
        self.status = novo_status

    def transferir(self, novo_usuario: str):
        ultimo = self.historico.obter_ultimo_registro()
        usuario_anterior = ultimo.usuario_atual if ultimo else None

        from .registro_historico import RegistroHistorico
        registro = RegistroHistorico(
            usuario_atual=novo_usuario,
            usuario_anterior=usuario_anterior
        )

        self.historico.inserir_registro(registro)

    def obter_dados(self):
        return {
            "serial": self.serial,
            "modelo": self.modelo,
            "status": self.status,
            "historico": self.historico.to_list()
        }
