from flask import (
    render_template,
    Blueprint,
)

bots = Blueprint('bots', __name__)

@bots.route('/list')
# @login_required
# @retrieve_data('list_bots')
def bots():
    return render_template('bots.html')