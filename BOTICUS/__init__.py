from msilib.schema import Environment
from flask import flask
import click
import os
app = Flask(__name__)

def config_sass():
    scss = Bundle('scss/main.scss', filters='pyscss', output='styles/css/main.css')
    assets = Environment(app)
    assets.debut=True
    assets.register('scss_main',scss)
    

from BOTICUS import routes