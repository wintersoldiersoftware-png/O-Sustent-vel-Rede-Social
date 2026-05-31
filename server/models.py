from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# 1. MODELO DE USUÁRIO
class Usuario(Base):
    __tablename__ = "USUARIO"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True, name="ID_USUARIO")
    nome = Column(String(100), name="NOME")
    email = Column(String(100), unique=True, name="EMAIL")
    data_nascimento = Column(DateTime, name="DATA_NASCIMENTO")
    senha_hash = Column(String(255), name="SENHA_HASH")
    data_criacao = Column(DateTime, default=datetime.utcnow, name="DATA_CRIACAO")

    # Relacionamento com as sessões (se o usuário for deletado, apaga as sessões dele)
    sessoes = relationship("SessaoLogin", back_populates="usuario", cascade="all, delete")


# 2. MODELO DE SESSÃO DE LOGIN
class SessaoLogin(Base):
    __tablename__ = "SESSAO_LOGIN"

    id_sessao = Column(Integer, primary_key=True, autoincrement=True, name="ID_SESSAO")
    id_usuario = Column(Integer, ForeignKey("USUARIO.ID_USUARIO", ondelete="CASCADE"), name="ID_USUARIO")
    token_sessao = Column(String(255), name="TOKEN_SESSAO")
    data_hora_login = Column(DateTime, default=datetime.utcnow, name="DATA_HORA_LOGIN")

    # Relacionamento de volta para o usuário
    usuario = relationship("Usuario", back_populates="sessoes")
