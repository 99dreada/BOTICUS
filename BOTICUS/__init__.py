from flask import Flask
from flask.cli import AppGroup
import click
import os
from BOTICUS.model import db

app = Flask(__name__)

def config_db(db_url='sqlite:///db/boticus.db'):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if app.config.get('PROFILE', False): # pragma: no cover
        from werkzeug.contrib.profiler import ProfilerMiddleware
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
    app.secret_key = "#########"
    db.init_app(app)

config_db()

app.config['BOTICUS_REFRESH'] = os.environ.get('BOTICUS_REFRESH', 30)

from BOTICUS import routes

db_cli = AppGroup('db')

@db_cli.command('init')
def db_init():
    try: os.mkdir('boticus/db')
    except: pass
    from BOTICUS.model import create_db
    create_db()

app.cli.add_command(db_cli)
