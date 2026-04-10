from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class TermoDevolucaoModel(Base):
    __tablename__ = "termos_devolucao"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"), nullable=False)
    responsavel = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    unidade = Column(String, nullable=False)
    data_devolucao = Column(String, nullable=False)
    estado_aparelho = Column(String, nullable=False)
    observacoes = Column(Text, nullable=True)

    dispositivo = relationship("DispositivoModel", back_populates="termos_devolucao")
