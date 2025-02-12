from flask import Flask, session, request, \
    render_template, url_for, redirect, flash
from banco import Conexao
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from User import User

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ULTRAMEGADIFICIL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(matricula):
    return User.get(matricula)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():

    if current_user:
        return redirect(url_for('home'))
    if request.method == 'POST':
        matricula = request.form['matricula']
        nome = request.form['nome']
        senha = generate_password_hash(request.form['senha'])

        if not User.exists(matricula): #Se o usuário não tiver cadastro
            user = User(matricula = matricula, nome = nome, senha = senha)
            user.save()
            # Logar o usuário depois de cadastrar
            login_user(user)
            return redirect(url_for('login'))
        
        else:
            return render_template('index.html')
        
    return render_template('register.html')
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user:
        return redirect(url_for('home'))
    if request.method == 'POST':
        matricula = request.form['matricula']
        senha = request.form['senha']
        usuario = User.get_by_mat(matricula)

        if check_password_hash(usuario['senha'], senha):  # Se o usuário for encontrado
                login_user(User.get(usuario['matricula']))

                return redirect(url_for('home'))
        
        else:
            return 'lascou'

    return render_template('login.html')


@app.route('/home', methods = ['GET'])
@login_required
def home():
    usu_nome = current_user.nome
    return render_template('home.html', usu_nome = usu_nome)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))