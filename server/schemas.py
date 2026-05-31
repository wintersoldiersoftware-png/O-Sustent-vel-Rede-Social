from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# --- SCHEMAS DE AUTENTICAÇÃO (Cadastro e Login) ---

# O que o Front-end precisa enviar para cadastrar um usuário
class UsuarioCadastro(BaseModel):
    nome: str
    email: EmailStr
    data_nascimento: date
    senha: str

# O que a API devolve de resposta após o cadastro (escondendo a senha por segurança)
class UsuarioResposta(BaseModel):
    id_usuario: int
    nome: str
    email: EmailStr
    data_criacao: datetime

    class Config:
        from_attributes = True  # Permite que o Pydantic leia os dados do SQLAlchemy (models.py)

# Estrutura do Token que o servidor devolve quando o Login dá certo
class Token(BaseModel):
    access_token: str
    token_type: str


# --- SCHEMAS DE PUBLICAÇÃO (Para o Feed de Notícias) ---

# O que o usuário envia para criar uma nova publicação ecológica
class PublicacaoCriar(BaseModel):
    conteudo: Optional[str] = None
    url_midia: Optional[str] = None
    tipo_midia: Optional[str] = None

# Como a publicação é devolvida para o feed
class PublicacaoResposta(BaseModel):
    id_publicacao: int
    id_usuario: int
    conteudo: Optional[str]
    url_midia: Optional[str]
    tipo_midia: Optional[str]
    data_publicacao: datetime

    class Config:
        from_attributes = True