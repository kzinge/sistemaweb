from flask import Flask, session, request, \
    render_template, url_for, redirect, flash
from bib import Conexao
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
conn = Conexao('banco.db')


# chave para critografia de cookies na sessão
app.config['SECRET_KEY'] = 'superdificil'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', nome=session['user'])

@app.route('/login', methods=['POST', 'GET'])
def login():
    # se já tá logado
    if 'user' in session:
        return redirect (url_for('dash')) #vai pra o dashboard

    # se não estiver logado
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        nome = request.form['nome']
        senha = request.form['senha']
        usuarios = conn.cursor.execute('SELECT usu_nome, usu_senha FROM tb_usuarios').fetchall()

        for usuario in usuarios:
            if usuario[0] == nome and check_password_hash(usuario[1], senha): #verifica se a senha enviada é igual a criptografia
                session['user'] = nome
                return redirect(url_for('dash'))
            
        flash("SENHA INCORRETA ou não está cadastrado. <a href='" + url_for('register') + "'>Cadastre-se aqui</a>", "error")
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():

    # se já tá logado
    if 'user' in session:
        return redirect (url_for('dash')) #vai pra o dashboard

    # se não estiver logado
    elif request.method == 'GET':
        return render_template('register.html')
    else:
        
        nome = request.form['nome']
        senha = generate_password_hash(request.form['senha']) #criptografar senha
        usuario = conn.cursor.execute('SELECT usu_nome FROM tb_usuarios WHERE usu_nome = (?)', (nome,)).fetchall()
        
        if not usuario:
            INSERT = "INSERT INTO tb_usuarios (usu_nome, usu_senha) VALUES (?, ?)"
            conn.cursor.execute(INSERT, (nome, senha))
            conn.commit()
        else:
            # flash messages
            return redirect(url_for('login')) 

        session['user'] = nome
        return redirect(url_for('dash'))

        
@app.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))