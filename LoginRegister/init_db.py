import sqlite3

conn = sqlite3.connect('banco.db')

TASK = 'banco.sql'

with open(TASK) as db:
    conn.executescript(db.read())

conn.commit()
conn.close()