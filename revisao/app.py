from flask import Flask, render_template, redirect, url_for, request
from database import db
from models.clientes import Cliente
from models.veiculos import Veiculo
from models.locacao import Locacao
from models.formcli import RegisterForm, VeiculosForm, LocacaoForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///revisao.db'
app.config['SECRET_KEY'] = 'supermegadificil    '

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    clientes = db.session.query(Cliente)
    veiculos = db.session.query(Veiculo)
    locacoes = db.session.query(Locacao)
    return render_template('index.html', clientes=clientes, veiculos=veiculos, locacoes=locacoes)

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():

    form = RegisterForm()

    if form.validate_on_submit(): 
        nome = form.nome.data
        email = form.email.data
        
        novo_cliente = Cliente(nome = nome, email = email)
        db.session.add(novo_cliente)
        db.session.commit()
        db.session.close()

        return redirect(url_for('index'))
    
    return render_template('cadastro.html', form = form)

@app.route('/cadastrar_veiculos', methods = ['GET', 'POST'])
def cadastrar_veiculos():

    form = VeiculosForm()

    if form.validate_on_submit(): 
        nome = form.nome.data
        
        novo_veiculo = Veiculo(nome = nome)
        db.session.add(novo_veiculo)
        db.session.commit()
        db.session.close()

        return redirect(url_for('index'))
    
    return render_template('veiculo.html', form = form)

@app.route('/locacao', methods = ['GET', 'POST'])
def locacao():

    form = LocacaoForm()

    if form.validate_on_submit(): 
        data = form.data_locacao.data
        cli_id = form.cliente_id.data
        vei_id = form.veiculo_id.data
        
        nova_locacao = Locacao(data = data, cliente_id = cli_id, veiculo_id = vei_id)
        db.session.add(nova_locacao)
        db.session.commit()
        db.session.close()

        return redirect(url_for('index'))
    
    return render_template('locacao.html', form = form)
