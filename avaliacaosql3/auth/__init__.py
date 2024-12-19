from flask_login import LoginManager
from ..models.user import User
from ..database.config import session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user