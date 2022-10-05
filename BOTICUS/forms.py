from wtforms_alchemy import ModelForm
from BOTICUS.model import (
    Bot_sql,
)

class Bot_Form(ModelForm):
    class Meta:
        model = Bot_sql