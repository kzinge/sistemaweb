from .controllers.new import new
from .controllers.user import user
from .auth import login_manager
from .auth.routes import auth_bp
from flask import Flask

# importar Base e engine
from .database.config import Base, engine

# Inicializa a apliacação
app = Flask(__name__)
app.config['SECRET_KEY'] = '123123123123'

# crair o banco com Base.medatada.create_all()
Base.metadata.create_all(bind = engine)

# Inicializa o controle de sessões
login_manager.init_app(app)

# Registra as rotas da aplicação
app.register_blueprint(new)
app.register_blueprint(user)

# Registra rotas de login/logout
app.register_blueprint(auth_bp)
