from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .database import Base


class DispositivoModel(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    serial = Column(String, unique=True, index=True, nullable=False)
    modelo = Column(String, nullable=False)
    status = Column(String, nullable=False)
    unidade = Column(String, nullable=False)

    historico = relationship("RegistroHistoricoModel", back_populates="dispositivo", cascade="all, delete-orphan")
    termos_aquisicao = relationship("TermoAquisicaoModel", back_populates="dispositivo", cascade="all, delete-orphan")
    termos_devolucao = relationship("TermoDevolucaoModel", back_populates="dispositivo", cascade="all, delete-orphan")
