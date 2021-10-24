from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
 
class LoginForm(FlaskForm):
    email = StringField("Email: ")
    psw = StringField("Пароль: ")
    submit = SubmitField("Войти")