from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Cadastrar')

class VeiculosForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class LocacaoForm(FlaskForm):
    data_locacao = DateField('Data')
    cliente_id = IntegerField('Cliente')
    veiculo_id = IntegerField('Veiculo')
    submit = SubmitField('Locar')