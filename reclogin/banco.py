import sqlite3 

class Conexao: 
    def __init__(self, db_name):

        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
    
    def close(self):

        if self.connection:
            self.connection.close()
    
    def commit(self):

        self.connection.commit()