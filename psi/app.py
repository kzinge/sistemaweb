from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

def obter_conexao():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/create', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        nome = request.form.get('nome')
        conn = obter_conexao()
        conn.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('pages/create-user.html')

@app.route('/usuarios')
def view_users():
    conn = obter_conexao()
    usarios = conn.execute('SELECT * FROM usuarios').fetchall()

    return render_template('pages/usuarios.html', users = usarios)

@app.route('/<int:id>/user', methods = ['GET', 'POST'])
def user(id):
    if request.method == 'POST':
        return render_template('pages/novapeca.html')
    conn = obter_conexao()
    pessoa = conn.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchall()
    
    return render_template('pages/user.html', pessoa = pessoa)

@app.route('/<int:id>/peca', methods = ['POST'])
def new_peca(id):
    conn = obter_conexao()
    novapeca = request.form.get('peca')
    conn.execute("INSERT INTO usuarios (peca) VALUES (?) WHERE id = (?)", (novapeca, id))
    conn.commit()
    return redirect(url_for('user'))


