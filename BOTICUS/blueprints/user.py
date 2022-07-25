from flask import Blueprint, render_template
from flask_login import current_user

user = Blueprint('user', __name__)

@user.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('user/login.html')