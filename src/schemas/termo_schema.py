from pydantic import BaseModel

class TermoAquisicaoCreate(BaseModel):
    serial: str
    responsavel: str
    cpf: str
    matricula: str
    telefone: str
    unidade: str
    data_aquisicao: str
    observacoes: str


class TermoDevolucaoCreate(BaseModel):
    serial: str
    responsavel: str
    cpf: str
    matricula: str
    telefone: str
    unidade: str
    data_devolucao: str
    estado_aparelho: str
    observacoes: str
