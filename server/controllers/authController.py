from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import bcrypt
import jwt  # Se for usar JWT mais para frente, ou apenas o token simples por enquanto
from datetime import datetime, timedelta

import models
import schemas

class AuthController:

    @staticmethod
    def hash_senha(senha: str) -> str:
        """Transforma a senha em texto limpo em um hash seguro usando Bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def verificar_senha(senha_limpa: str, senha_hash: str) -> bool:
        """Verifica se a senha digitada no login bate com o hash salvo no banco."""
        return bcrypt.checkpw(senha_limpa.encode('utf-8'), senha_hash.encode('utf-8'))

    @staticmethod
    def cadastrar_usuario(dados: schemas.UsuarioCadastro, db: Session):
        """Verifica se o e-mail já existe e salva o novo usuário no MySQL."""
        
        # 1. Verificar se o e-mail já está cadastrado
        usuario_existente = db.query(models.Usuario).filter(models.Usuario.email == dados.email).first()
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este e-mail já está cadastrado no Ser Sustentável."
            )
        
        # 2. Criptografar a senha
        senha_criptografada = AuthController.hash_senha(dados.senha)
        
        # 3. Criar o objeto do modelo SQLAlchemy
        novo_usuario = models.Usuario(
            nome=dados.nome,
            email=dados.email,
            data_nascimento=dados.data_nascimento,
            senha_hash=senha_criptografada
        )
        
        # 4. Salvar no banco de dados
        try:
            db.add(novo_usuario)
            db.commit()
            db.refresh(novo_usuario)  # Recupera o ID gerado pelo MySQL
            return novo_usuario
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao salvar no banco de dados: {str(e)}"
            )

    @staticmethod
    def login_usuario(form_data, db: Session):
        """Valida as credenciais do usuário e finge a geração do token para a Sprint 1."""
        usuario = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()
        
        if not usuario or not AuthController.verificar_senha(form_data.password, usuario.senha_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha incorretos.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Cria um token simples ou simulado para cumprir o schema da Sprint 1
        token_simulado = f"token_usuario_{usuario.id_usuario}_{datetime.utcnow().strftime('%Y%m%d%H%M')}"
        
        # Salva a sessão na tabela SESSAO_LOGIN
        nova_sessao = models.SessaoLogin(
            id_usuario=usuario.id_usuario,
            token_sessesao=token_simulado  # Nota: ajuste o nome da coluna se houver typo no SQL
        )
        db.add(nova_sessao)
        db.commit()

        return {"access_token": token_simulado, "token_type": "bearer"}