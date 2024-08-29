import sqlite3

class Conexao():
    def __init__(self, banco):
        self.banco = banco

    def conexao(self):
        conn = sqlite3.connect(self.banco)