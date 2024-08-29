from flask import Flask, render_template, redirect, url_for, request #Importar bib flask e funções
from conexao import Conexao #Importa uma bib que eu fiz para agilizar a conexão do banco

app = Flask(__name__) #Define nosso app
conn = Conexao('escola.db') #Define nossa conexão com o banco, lembrar que o nome do banco é dentro dos () 

@app.route('/') #Define a primeira rota
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET']) #Define a rota cadastro que pode ser GET e POST
def cadastrar():
    if request.method == 'POST': #Caso a rota seja usada pelo método POST (formulário)
        nome = request.form.get('alunome') #pegando informações do meu formulário da pagina cadastro.html
        email = request.form.get('aluemail') #pegando informações do meu formulário da pagina cadastro.html
        telefone = request.form.get('alutel') #pegando informações do meu formulário da pagina cadastro.html

        #Inserindo informações no banco
        conn.cursor.execute('INSERT INTO tb_alunos (alu_nome, alu_email, alu_telefone) VALUES (?,?,?)', (nome, email, telefone,))
        #Salvando informações
        conn.commit()
        return redirect(url_for('index'))
    
    #Caso seja acessado pelo GET:
    return render_template('cadastro.html')

@app.route('/alunos') #Define a rota alunos
def view_alunos():
    #Monstrando as informações do banco
    alunos = conn.cursor.execute('SELECT alu_nome, alu_email, alu_telefone FROM tb_alunos').fetchall()

    return render_template('view.html', alunos = alunos)
#esse 'alunos = alunos': o primeiro alunos é a variável que irei usar em view.html. o segundo é o valor que irei atribuir a ela.
