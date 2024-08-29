CREATE TABLE IF NOT EXISTS tb_alunos (
    alu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alu_nome TEXT NOT NULL,
    alu_email TEXT NOT NULL,
    alu_telefone TEXT NOT NULL
);