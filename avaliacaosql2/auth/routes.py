from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, LoginManager, current_user
from core.models import User
from database.config import session
from sqlalchemy import select

auth_bp = Blueprint('auth', 'auth', template_folder='templates')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('core.users'))
    
    elif request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        # fazer a busca no banco pelo usuário pelo nome
        busca = session.execute(select(User).where(User.nome == nome, User.senha == senha)).first()
        # Aqui você precisa de fato pegar o usuário no banco e logar ele
        if busca == None:
                return redirect(url_for('auth.register'))
        elif busca[0]:
            login_user(busca[0])
            return redirect(url_for('core.users'))

        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        busca = session.execute(select(User).where(User.email == email)).first()
        if busca == None:
            user = User(nome, email, senha)
            session.add(user)
            session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Esse e-mail já está cadastrado', 'error')
            return render_template('register.html')
        
    return render_template('register.html')
    


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))
