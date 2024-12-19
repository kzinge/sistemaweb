from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import select
from database.config import session
from core.models import User, Noticia
from datetime import datetime

core = Blueprint('core', 'core', template_folder='templates')

@core.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('core.users'))
    
    return render_template('index.html')

@core.route('/users')
@login_required
def users():
    usuarios = session.execute(select(User)).scalars().all()
    return render_template('core/users.html', usuarios = usuarios)

@core.route('/noticias')
def noticias():
    noticias = session.execute(select(Noticia, User.nome).join(User, User.id == Noticia.user_id)).all()
    return render_template('core/index.html', noticias = noticias)

@core.route('/novanoticia', methods = ['POST', 'GET'])
def newnotice():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
        descricao = request.form['descricao']
        user_id = current_user.id

        noticia = Noticia(titulo, data, descricao, user_id)
        session.add(noticia)
        session.commit()

        return redirect(url_for('core.noticias'))
    
    else:
        return render_template('core/newnoticia.html')