from sqlalchemy.orm import Session
from datetime import datetime
from src.classes.dispositivo import Dispositivo
from src.classes.registro_historico import RegistroHistorico as RegistroHistoricoClass
from src.models import DispositivoModel, RegistroHistoricoModel, TermoAquisicaoModel, TermoDevolucaoModel


class DispositivoRepository:
    def __init__(self, db: Session):
        self.db = db

    def adicionar(self, dispositivo: Dispositivo):
        db_dispositivo = DispositivoModel(
            serial=dispositivo.serial,
            modelo=dispositivo.modelo,
            status=dispositivo.status,
            unidade=dispositivo.unidade
        )
        self.db.add(db_dispositivo)
        self.db.commit()
        self.db.refresh(db_dispositivo)
        return db_dispositivo

    def buscar(self, serial: str):
        db_dispositivo = self.db.query(DispositivoModel).filter(DispositivoModel.serial == serial).first()
        if not db_dispositivo:
            return None

        return self._model_to_object(db_dispositivo)

    def atualizar(self, dispositivo: Dispositivo):
        db_dispositivo = self.db.query(DispositivoModel).filter(DispositivoModel.serial == dispositivo.serial).first()
        if db_dispositivo:
            db_dispositivo.status = dispositivo.status
            self.db.commit()
            self.db.refresh(db_dispositivo)

    def adicionar_historico(self, serial: str, registro: RegistroHistoricoClass):
        db_dispositivo = self.db.query(DispositivoModel).filter(DispositivoModel.serial == serial).first()
        if db_dispositivo:
            data_trans = registro.data_transferencia
            if isinstance(data_trans, str):
                data_trans = datetime.fromisoformat(data_trans)

            db_registro = RegistroHistoricoModel(
                dispositivo_id=db_dispositivo.id,
                usuario_atual=registro.usuario_atual,
                usuario_anterior=registro.usuario_anterior,
                data_transferencia=data_trans
            )
            self.db.add(db_registro)
            self.db.commit()

    def adicionar_termo_aquisicao(self, serial: str, termo_data: dict):
        db_dispositivo = self.db.query(DispositivoModel).filter(DispositivoModel.serial == serial).first()
        if db_dispositivo:
            db_termo = TermoAquisicaoModel(
                dispositivo_id=db_dispositivo.id,
                responsavel=termo_data["responsavel"],
                cpf=termo_data["cpf"],
                matricula=termo_data["matricula"],
                telefone=termo_data["telefone"],
                unidade=termo_data["unidade"],
                data_aquisicao=termo_data["data_aquisicao"],
                observacoes=termo_data["observacoes"]
            )
            self.db.add(db_termo)
            self.db.commit()

    def adicionar_termo_devolucao(self, serial: str, termo_data: dict):
        db_dispositivo = self.db.query(DispositivoModel).filter(DispositivoModel.serial == serial).first()
        if db_dispositivo:
            db_termo = TermoDevolucaoModel(
                dispositivo_id=db_dispositivo.id,
                responsavel=termo_data["responsavel"],
                cpf=termo_data["cpf"],
                matricula=termo_data["matricula"],
                telefone=termo_data["telefone"],
                unidade=termo_data["unidade"],
                data_devolucao=termo_data["data_devolucao"],
                estado_aparelho=termo_data["estado_aparelho"],
                observacoes=termo_data["observacoes"]
            )
            self.db.add(db_termo)
            self.db.commit()

    def listar(self):
        db_dispositivos = self.db.query(DispositivoModel).all()
        return [self._model_to_object(db_disp) for db_disp in db_dispositivos]

    def _model_to_object(self, db_dispositivo: DispositivoModel) -> Dispositivo:
        dispositivo = Dispositivo(
            serial=db_dispositivo.serial,
            modelo=db_dispositivo.modelo,
            status=db_dispositivo.status,
            unidade=db_dispositivo.unidade
        )

        for db_registro in db_dispositivo.historico:
            registro = RegistroHistoricoClass(
                usuario_atual=db_registro.usuario_atual,
                usuario_anterior=db_registro.usuario_anterior
            )
            registro.data_transferencia = db_registro.data_transferencia.isoformat()
            dispositivo.historico.inserir_registro(registro)

        return dispositivo
