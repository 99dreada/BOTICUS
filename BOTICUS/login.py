from flask_login import LoginManager

login_manager = LoginManager()

def login_init_app(app):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'info'
