from flask import Flask, render_template, redirect, url_for, request
from conexao import Conexao

app = Flask(__name__)
conn = Conexao('escola.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('alunome')
        email = request.form.get('aluemail')
        telefone = request.form.get('alutel')
        conn.cursor.execute('INSERT INTO tb_alunos (alu_nome, alu_email, alu_telefone) VALUES (?,?,?)', (nome, email, telefone,))
        conn.commit()
        return redirect(url_for('index'))
    
    return render_template('cadastro.html')

@app.route('/alunos')
def view_alunos():
    alunos = conn.cursor.execute('SELECT alu_nome, alu_email, alu_telefone FROM tb_alunos').fetchall()

    return render_template('view.html', alunos = alunos)
