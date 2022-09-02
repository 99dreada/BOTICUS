from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    validators,
)
from flask_wtf import FlaskForm
from BOTICUS import app

class Login_Form(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')