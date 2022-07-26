from flask import Blueprint, render_template
from flask_login import current_user
from BOTICUS.util import (
    dict_but
)

from BOTICUS.forms import (
    Login_Form
)

user = Blueprint('user', __name__)

@user.route("/login", methods=['GET', 'POST'])
def login():
    form = Login_Form()
    return render_template('user/login.html', title='Login', form=form)