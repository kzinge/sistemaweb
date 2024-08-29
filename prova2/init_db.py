import sqlite3

#conectar/ativar o banco

conn = sqlite3.connect('escola.db')

BANCO = 'escola.sql'

with open(BANCO) as db:
    conn.executescript(db.read())

conn.commit()
conn.close()