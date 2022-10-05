from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash,
    Blueprint,

)
from flask_login import login_required, login_user, logout_user, current_user
from wtforms import (
    validators,
)
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
def load_user(id):
    return User_sql.query.get(int(id))

@user.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print("test0")
        print(current_user + "something")
        return redirect(url_for("bots"))
    form = Login_Form()
    print("test1")
    if request.method == 'GET':
        print("test2")
        pass
    elif form.validate_on_submit():
        print("test3")
        user = User_sql.query.filter_by(Username=form.Username.data).first()
        if user and form.Password.data:
            print("test4")
            login_user(user, remember=form.remember.data)
            return redirect(url_for("bots"))
        else:
            flash('Login Unsuccessful. please check username and password', 'danger')
    return render_template('user/login.html', title='Login', form=form)

@user.route("/logout")
@login_required
def logout():
        logout_user()
        return redirect("login")
