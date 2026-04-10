from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schemas.dispositivo_schema import DispositivoCreate
from src.schemas.transferencia_schema import TransferenciaCreate
from src.schemas.termo_schema import TermoAquisicaoCreate, TermoDevolucaoCreate
from src.repository.dispositivo_repo import DispositivoRepository
from src.service.dispositivo_service import DispositivoService
from src.models import get_db

router = APIRouter()


def get_service(db: Session = Depends(get_db)):
    repo = DispositivoRepository(db)
    return DispositivoService(repo)


@router.post("/dispositivos")
def criar_dispositivo(data: DispositivoCreate, service: DispositivoService = Depends(get_service)):
    try:
        return service.criar_dispositivo(data).obter_dados()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/transferencias")
def transferir(data: TransferenciaCreate, service: DispositivoService = Depends(get_service)):
    try:
        return service.transferir(data.serial, data.novo_usuario).obter_dados()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/termos/aquisicao")
def termo_aquisicao(data: TermoAquisicaoCreate, service: DispositivoService = Depends(get_service)):
    try:
        termo = service.gerar_termo_aquisicao(data)
        return termo.obter_termo()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/termos/devolucao")
def termo_devolucao(data: TermoDevolucaoCreate, service: DispositivoService = Depends(get_service)):
    try:
        termo = service.gerar_termo_devolucao(data)
        return termo.obter_termo()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/dispositivos/{serial}")
def obter_dispositivo(serial: str, service: DispositivoService = Depends(get_service)):
    try:
        return service.obter_dispositivo(serial)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/dispositivos")
def listar(service: DispositivoService = Depends(get_service)):
    return service.listar()
