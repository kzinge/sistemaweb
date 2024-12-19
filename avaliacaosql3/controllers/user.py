from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import select
from ..database.config import session
from ..models.user import User

user = Blueprint('user', 'user', template_folder='controllers/templates')

@user.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('user.users'))
    
    return render_template('index.html')

@user.route('/users')
@login_required
def users():
    usuarios = session.execute(select(User)).scalars().all()
    return render_template('users.html', usuarios = usuarios)