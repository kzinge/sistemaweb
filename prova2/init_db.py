import sqlite3 #importa a bib sqlite

#conectar/ativar o banco

conn = sqlite3.connect('escola.db') #conexão com o banco

BANCO = 'escola.sql' #define qual banco irei usar

with open(BANCO) as db:
    conn.executescript(db.read()) #ler o banco

conn.commit() #salvar alterações
conn.close() #fechar o banco