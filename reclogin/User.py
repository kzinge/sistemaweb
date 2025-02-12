from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

database = 'database.db'

def get_conexao():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self, **kwargs):
        if 'matricula' in kwargs.keys():
            self.matricula = kwargs['matricula']
        
        if 'nome' in kwargs.keys():
            self.nome = kwargs['nome']

        if 'senha' in kwargs.keys():
            self.senha = kwargs['senha']

    def get_id(self):
        return str(self.matricula)

    @classmethod
    def get(cls,matricula): #pegar os dados de um usuário
        cursor = get_conexao()
        user = cursor.execute("SELECT * FROM tb_usuarios WHERE matricula = ?", (matricula,)).fetchone()
        cursor.close()
        
        if user:
            loaduser = User(matricula = user['matricula'], nome=user['nome'], senha=user['senha'])
            loaduser.matricula = user['matricula']
            return loaduser
        else:
            return None
        
    @classmethod
    def get_by_mat(cls,mat):
        conn = get_conexao()
        user = conn.execute("SELECT * FROM tb_usuarios WHERE matricula = ?", (mat,)).fetchone()
        conn.close()
        return user
        
    @classmethod
    def exists(cls, matricula): #Verificar se usário existe
        cursor = get_conexao()
        user = cursor.execute("SELECT * FROM tb_usuarios WHERE matricula = ?", (matricula,)).fetchone()
        cursor.close()
        if user: 
            return True
        else:
            return False
    
    def save(self):   #Salvar os dados  
        cursor = get_conexao() 
        cursor.execute("INSERT INTO tb_usuarios(matricula, nome, senha) VALUES (?, ?, ?)", (self.matricula, self.nome, self.senha))
        # salva o id no objeto recem salvo no banco
        cursor.commit()
        cursor.close()
        return True