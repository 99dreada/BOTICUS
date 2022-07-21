from flask import(
    render_template,
)
from flask_login import login_required
from BOTICUS import app


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

@app.route('/login')
def login():
    return render_template('login.html')