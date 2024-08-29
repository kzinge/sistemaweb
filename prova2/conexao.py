import sqlite3 #importa o sqlite

class Conexao: #classe para fazer a conexão
    def __init__(self, db_name):
        #Inicializa a conexão com o banco de dados.
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row #Isso serve para que possamos usar o nome da coluna do banco como paramentro no view.html
        self.cursor = self.connection.cursor()
    
    def close(self):
        #Fecha a conexão com o banco de dados.
        if self.connection:
            self.connection.close()
    
    def commit(self):
        #Comita uma ação no banco
        self.connection.commit()
