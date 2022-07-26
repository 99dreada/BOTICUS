from wtforms import(
    Form,
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    validators,
)
from flask_wtf import FlaskForm

class Login_Form(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')