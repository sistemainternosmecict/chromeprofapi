from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class RegistroHistoricoModel(Base):
    __tablename__ = "registro_historico"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"), nullable=False)
    usuario_atual = Column(String, nullable=False)
    usuario_anterior = Column(String, nullable=True)
    data_transferencia = Column(DateTime, default=datetime.utcnow, nullable=False)

    dispositivo = relationship("DispositivoModel", back_populates="historico")
