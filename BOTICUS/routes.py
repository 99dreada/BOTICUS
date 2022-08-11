from flask import(
    render_template,
)
from flask_login import current_user, login_required
from BOTICUS import app
import BOTICUS.blueprints


"""
ROUTING
"""
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bots')
@login_required
def bots():
    return render_template('bots.html')

@app.route('/content')
@login_required
def content():
    return render_template('content.html')

"""
Blueprint registation
"""
app.register_blueprint(BOTICUS.blueprints.user, url_prefix='/User')