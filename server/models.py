from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# --- TABELA DE CURTIDAS (Relacionamento N:M - Associação) ---
class Curtida(Base):
    __tablename__ = "CURTIDA"
    
    id_usuario = Column(Integer, ForeignKey("USUARIO.ID_USUARIO", ondelete="CASCADE"), primary_key=True, name="ID_USUARIO")
    id_publicacao = Column(Integer, ForeignKey("PUBLICACAO.ID_PUBLICACAO", ondelete="CASCADE"), primary_key=True, name="ID_PUBLICACAO")


# --- 1. TABELA DE USUÁRIOS ---
class Usuario(Base):
    __tablename__ = "USUARIO"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True, name="ID_USUARIO")
    nome = Column(String(100), nullable=False, name="NOME")
    email = Column(String(100), unique=True, nullable=False, name="EMAIL")
    data_nascimento = Column(DateTime, nullable=False, name="DATA_NASCIMENTO")
    senha_hash = Column(String(255), nullable=False, name="SENHA_HASH")
    data_criacao = Column(DateTime, default=datetime.utcnow, name="DATA_CRIACAO")

    # Relacionamentos (permite que o FastAPI aceda às publicações do utilizador facilmente)
    publicacoes = relationship("Publicacao", back_populates="autor", cascade="all, delete")
    comentarios = relationship("Comentario", back_populates="autor", cascade="all, delete")


# --- 2. TABELA DE PUBLICAÇÕES ---
class Publicacao(Base):
    __tablename__ = "PUBLICACAO"

    id_publicacao = Column(Integer, primary_key=True, autoincrement=True, name="ID_PUBLICACAO")
    id_usuario = Column(Integer, ForeignKey("USUARIO.ID_USUARIO", ondelete="CASCADE"), nullable=False, name="ID_USUARIO")
    conteudo = Column(Text, nullable=True, name="CONTEUDO")
    url_midia = Column(String(255), nullable=True, name="URL_MIDIA")
    tipo_midia = Column(String(50), nullable=True, name="TIPO_MIDIA")
    data_publicacao = Column(DateTime, default=datetime.utcnow, name="DATA_PUBLICACAO")

    # Relacionamentos
    autor = relationship("Usuario", back_populates="publicacoes")
    comentarios = relationship("Comentario", back_populates="publicacao", cascade="all, delete")


# --- 4. TABELA DE COMENTÁRIOS ---
class Comentario(Base):
    __tablename__ = "COMENTARIO"

    id_comentario = Column(Integer, primary_key=True, autoincrement=True, name="ID_COMENTARIO")
    id_usuario = Column(Integer, ForeignKey("USUARIO.ID_USUARIO", ondelete="CASCADE"), nullable=False, name="ID_USUARIO")
    id_publicacao = Column(Integer, ForeignKey("PUBLICACAO.ID_PUBLICACAO", ondelete="CASCADE"), nullable=False, name="ID_PUBLICACAO")
    conteudo = Column(Text, nullable=False, name="CONTEUDO")
    data_comentario = Column(DateTime, default=datetime.utcnow, name="DATA_COMENTARIO")

    # Relacionamentos
    autor = relationship("Usuario", back_populates="comentarios")
    publicacao = relationship("Publicacao", back_populates="comentarios")