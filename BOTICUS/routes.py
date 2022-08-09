from flask import(
    render_template,
)
from BOTICUS import app
import BOTICUS.blueprints


"""
ROUTING
"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

@app.route('/content')
def content():
    return render_template('content.html')

"""
Blueprint registation
"""
app.register_blueprint(BOTICUS.blueprints.user, url_prefix='/User')