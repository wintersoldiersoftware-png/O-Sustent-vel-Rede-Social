from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa a conexão do banco para garantir que as tabelas sejam reconhecidas
from database import engine
import models

# Importa o módulo de rotas de autenticação que criaste
from routes.auth_routes import router as auth_router

# Cria a aplicação FastAPI com metadados do teu projeto ecológico
app = FastAPI(
    title="Ser Sustentável API 🌿",
    description="API para a rede social ecológica Ser Sustentável, gerenciando usuários, publicações e interações.",
    version="1.0.0"
)

# --- CONFIGURAÇÃO DE CORS ---
# Permite que o teu Front-end (que estará rodando na pasta public/ via Live Server)
# consiga fazer requisições para este Back-end sem ser bloqueado pelo navegador.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitui pelo link oficial do teu site
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

# --- INCLUSÃO DAS ROTAS ---
# Vincula as rotas de autenticação (/auth/cadastro e /auth/login) ao servidor principal
app.include_router(auth_router)

# Rota inicial padrão apenas para testar se o servidor está online
@app.get("/", tags=["Raiz"])
def verificar_servidor():
    return {
        "status": "online",
        "mensagem": "Servidor da rede social Ser Sustentável está rodando perfeitamente!"
    }