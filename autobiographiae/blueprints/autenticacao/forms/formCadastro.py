from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, FileField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileAllowed

class CadastroForm(FlaskForm):
    foto = FileField(label='Foto:', name='foto', id="foto", validators=[FileAllowed('jpg', 'png')])
    nome = StringField(label='Nome:', name='nome', validators=[DataRequired()], id="nome")
    email = EmailField(label='Email:', name='email', validators=[DataRequired(), Email()], id="email")
    senha = PasswordField(label='Senha:', name='senha', validators=[DataRequired(), EqualTo('confirm'), Length(min=8, max=50)], id="senha")
    confirm = PasswordField('Confirme a senha:', validators=[DataRequired(), Length(min=8, max=50)])
    recaptcha = RecaptchaField()