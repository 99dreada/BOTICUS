from flask import(
    render_template, url_for, request,
)
from flask_breadcrumbs import register_breadcrub
import boticus from app

@app.route('/', method=['GET','POST'])
@register_breadcrub(app, '.', 'Home')

def index():
    return render_template(
        'home.html',
        title='Home',
    )