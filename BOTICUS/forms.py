from wtforms import (
    BooleanField,
    SubmitField
)
from BOTICUS import app
from wtforms_alchemy import ModelForm

from BOTICUS.model import (
    User_sql,
)

class Login_Form(ModelForm):
    class Meta:
        model = User_sql
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')