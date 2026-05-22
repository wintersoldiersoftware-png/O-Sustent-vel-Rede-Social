-- -----------------------------------------------------
-- Tabela: USUARIO
-- -----------------------------------------------------
CREATE TABLE USUARIO (
    ID_USUARIO INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(150) NOT NULL,
    EMAIL VARCHAR(150) NOT NULL UNIQUE,
    DATA_NASCIMENTO DATE NOT NULL,
    SENHA_HASH VARCHAR(255) NOT NULL,
    DATA_CRIACAO DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------
-- Tabela: SESSAO_LOGIN
-- -----------------------------------------------------
CREATE TABLE SESSAO_LOGIN (
    ID_SESSAO INT AUTO_INCREMENT PRIMARY KEY,
    ID_USUARIO INT NOT NULL,
    TOKEN_SESSAO VARCHAR(255) NOT NULL,
    DATA_HORA_LOGIN DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_sessao_usuario 
        FOREIGN KEY (ID_USUARIO) 
        REFERENCES USUARIO(ID_USUARIO) 
        ON DELETE CASCADE
);

-- -----------------------------------------------------
-- Tabela: PUBLICACAO
-- -----------------------------------------------------
CREATE TABLE PUBLICACAO (
    ID_PUBLICACAO INT AUTO_INCREMENT PRIMARY KEY,
    ID_USUARIO INT NOT NULL,
    CONTEUDO TEXT NOT NULL,
    URL_MIDIA VARCHAR(255),
    TIPO_MIDIA VARCHAR(50),
    DATA_PUBLICACAO DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_publicacao_usuario 
        FOREIGN KEY (ID_USUARIO) 
        REFERENCES USUARIO(ID_USUARIO) 
        ON DELETE CASCADE
