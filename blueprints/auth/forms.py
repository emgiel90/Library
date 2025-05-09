from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from typing import Any

class RegistrationForm(FlaskForm):
    username: Any = StringField('Il tuo Username:', validators=[DataRequired(), Length(min=4, max=20)])
    email: Any = StringField('Email', validators=[DataRequired(), Email()])
    password: Any = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrati')



class LoginForm(FlaskForm):
    email: Any = StringField('Email', validators=[DataRequired(), Email()])
    password: Any = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Accedi')


class ForgotPasswordForm(FlaskForm):
    email: Any = StringField('Email', validators=[DataRequired(), Email(message='Email non valida')])
    submit = SubmitField('Vuoi recuperare la password?')
