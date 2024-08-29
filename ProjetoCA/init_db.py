import sqlite3

conn = sqlite3.connect('task.db')

TASK = 'task.sql'

with open(TASK) as db:
    conn.executescript(db.read())

conn.commit()
conn.close()