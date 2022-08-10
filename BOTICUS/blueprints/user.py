from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash,
    Blueprint,

)
from flask_login import login_user, current_user
from BOTICUS.login import login_manager
from BOTICUS.model import (
    db,
    User_sql,
)
from BOTICUS.util import (
    dict_but,
)

from BOTICUS.forms import (
    Login_Form
)

user = Blueprint('user', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User_sql.query.get(int(user_id))

@user.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("bots"))
    form = Login_Form()
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        print("yes")
        user = User_sql.query.filter_by(username=form.username.data).first()
        if user and form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for("bots"))
        else:
            flash('Login Unsuccessful. please check username and password', 'danger')
    return render_template('user/login.html', title='Login', form=form)