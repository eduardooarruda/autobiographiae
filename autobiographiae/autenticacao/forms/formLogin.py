from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField(label='Email:', name='email', validators=[DataRequired(), Email()], id="email")
    senha = PasswordField(label='Senha:', name='senha', validators=[DataRequired(), Length(min=8, max=50)], id="senha")