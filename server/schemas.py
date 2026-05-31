from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# Dados que o Front-end precisa enviar para cadastrar um usuário
class UsuarioCadastro(BaseModel):
    nome: str
    email: EmailStr
    data_nascimento: date
    senha: str

# Dados que a API vai devolver (Proteção de dados: Não devolvemos a Senha!)
class UsuarioResposta(BaseModel):
    id_usuario: int
    nome: str
    email: EmailStr
    data_criacao: datetime

    class Config:
        from_attributes = True

# Estrutura do Token que será devolvido no Login
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
