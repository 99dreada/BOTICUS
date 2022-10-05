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

app.register_blueprint(BOTICUS.blueprints.bot, url_prefix='/bot')