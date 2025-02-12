CREATE TABLE IF NOT EXISTS tb_usuarios (
    matricula TEXT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    senha TEXT NOT NULL
);