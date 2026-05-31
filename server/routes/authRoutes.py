from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Importamos a conexão do banco, os schemas e o controlador
from database import get_db
import schemas
from controllers.auth_controller import AuthController

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação - Sprint 1"]
)

# 1. Rota de Cadastro (Sign-up)
@router.post("/cadastro", response_model=schemas.UsuarioResposta, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: schemas.UsuarioCadastro, db: Session = Depends(get_db)):
    """
    Recebe os dados do formulário de cadastro do Front-end,
    valida via Pydantic e envia para o controlador salvar no MySQL.
    """
    return AuthController.cadastrar_usuario(dados, db)


# 2. Rota de Login (Sign-in)
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Recebe o e-mail (no campo username) e a senha.
    Se estiverem corretos, gera o token de acesso e cria a sessão no banco.
    """
    return AuthController.login_usuario(form_data, db)