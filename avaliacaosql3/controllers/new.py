from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import select
from ..database.config import session
from ..models.user import User
from ..models.new import Noticia
from datetime import datetime

new = Blueprint('new', 'new', template_folder='controllers/templates')

@new.route('/noticias')
@login_required
def noticias():
    noticias = session.execute(select(Noticia, User.nome).join(User, User.id == Noticia.user_id)).all()
    return render_template('noticias.html', noticias = noticias)

@new.route('/novanoticia', methods = ['POST', 'GET'])
@login_required
def newnotice():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
        descricao = request.form['descricao']
        user_id = current_user.id

        noticia = Noticia(titulo, data, descricao, user_id)
        session.add(noticia)
        session.commit()

        return redirect(url_for('new.noticias'))
    
    else:
        return render_template('newnoticia.html')