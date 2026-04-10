from src.repository.dispositivo_repo import DispositivoRepository
from src.classes.dispositivo import Dispositivo
from src.classes.aquisicao import Aquisicao
from src.classes.devolucao import Devolucao


class DispositivoService:
    def __init__(self, repo: DispositivoRepository):
        self.repo = repo

    def criar_dispositivo(self, data):
        dispositivo = Dispositivo(**data.dict())
        self.repo.adicionar(dispositivo)
        return dispositivo

    def transferir(self, serial: str, novo_usuario: str):
        dispositivo = self.repo.buscar(serial)
        if not dispositivo:
            raise ValueError("Dispositivo não encontrado")

        dispositivo.transferir(novo_usuario)

        ultimo_registro = dispositivo.historico.obter_ultimo_registro()
        if ultimo_registro:
            self.repo.adicionar_historico(serial, ultimo_registro)

        return dispositivo

    def gerar_termo_aquisicao(self, data):
        dispositivo = self.repo.buscar(data.serial)
        if not dispositivo:
            raise ValueError("Dispositivo não encontrado")

        termo = Aquisicao(
            dispositivo=dispositivo,
            responsavel=data.responsavel,
            cpf=data.cpf,
            matricula=data.matricula,
            telefone=data.telefone,
            unidade=data.unidade,
            data_aquisicao=data.data_aquisicao,
            observacoes=data.observacoes
        )

        dispositivo.transferir(data.responsavel)

        ultimo_registro = dispositivo.historico.obter_ultimo_registro()
        if ultimo_registro:
            self.repo.adicionar_historico(data.serial, ultimo_registro)

        termo_data = {
            "responsavel": data.responsavel,
            "cpf": data.cpf,
            "matricula": data.matricula,
            "telefone": data.telefone,
            "unidade": data.unidade,
            "data_aquisicao": data.data_aquisicao,
            "observacoes": data.observacoes
        }
        self.repo.adicionar_termo_aquisicao(data.serial, termo_data)

        return termo

    def gerar_termo_devolucao(self, data):
        dispositivo = self.repo.buscar(data.serial)
        if not dispositivo:
            raise ValueError("Dispositivo não encontrado")

        termo = Devolucao(
            dispositivo=dispositivo,
            responsavel=data.responsavel,
            cpf=data.cpf,
            matricula=data.matricula,
            telefone=data.telefone,
            unidade=data.unidade,
            data_devolucao=data.data_devolucao,
            estado_aparelho=data.estado_aparelho,
            observacoes=data.observacoes
        )

        dispositivo.atualizar_status("parado")
        self.repo.atualizar(dispositivo)

        termo_data = {
            "responsavel": data.responsavel,
            "cpf": data.cpf,
            "matricula": data.matricula,
            "telefone": data.telefone,
            "unidade": data.unidade,
            "data_devolucao": data.data_devolucao,
            "estado_aparelho": data.estado_aparelho,
            "observacoes": data.observacoes
        }
        self.repo.adicionar_termo_devolucao(data.serial, termo_data)

        return termo

    def obter_dispositivo(self, serial: str):
        dispositivo = self.repo.buscar(serial)
        if not dispositivo:
            raise ValueError("Dispositivo não encontrado")

        return dispositivo.obter_dados()

    def listar(self):
        return [d.obter_dados() for d in self.repo.listar()]
