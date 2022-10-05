from flask import (
    render_template,
    Blueprint,
    url_for,
    redirect,
    request,
    flash,
)
from BOTICUS.model import(
    db,
    Bot_sql,
)
from BOTICUS.util import(
    bulk_validate,
    create_forms,
    dict_except,
    form_to_db_fields,
    natural_to_surrogate_key,
    retrieve_data,
    form_from_db_fields,
)

bot = Blueprint('bot', __name__)


@bot.route("/list")
def list():
    bots = Bot_sql.query.all()
    return render_template('bot/list.html', title='List Bots', bots=bots)

@bot.route("/create", methods=['GET','POST'])
@create_forms('bot_form')
def create(forms):
    forms_only_show = ['bot_form']
    if request.method == 'GET':
        pass
    elif bulk_validate(dict_except(forms, forms_only_show)):
        try:
            new_bot = form_to_db_fields(Bot_sql, forms['bot_form'])
            db.session.commit()
            flash(f"Bot {new_bot.Name} has been successfully added ", "success",)
            return redirect(url_for('.list'))
        except Exception as e: # pragma: no cover
            flash(f"Bot creation not successful.\nError: {e}", "danger")
    return render_template(
        'bot/edit.html',
        title='Create Bot',
        action_mode='Create',
        **forms
    )

@bot.route('/<Name>/edit', methods=['GET','POST'])
@natural_to_surrogate_key(Bot_sql, 'Name')
@retrieve_data('current_bot')
@create_forms('bot_form')
def edit(Name, id, forms, dbvalues):
    forms_only_show = ['bot_form']
    bot = Bot_sql.query.get_or_404(id)
    if request.method == 'GET':
        form_from_db_fields(dbvalues['current_bot'], forms['bot_form'])
    elif bulk_validate(dict_except(forms, forms_only_show)):
        forms['bot_form'].populate_obj(dbvalues['current_bot'])
        try:
            db.session.commit()
            flash(f"Bot {Name} has been sucessfully amended", "success")
            return redirect(url_for('.list'))
        except Exception as e:
            flash(f"Bot amendment was unsuccessful.\nerror: {e}", "danger")
    return render_template(
        'bot/edit.html',
        title='Edit Bot',
        action_mode='Edit',
        name=Name,
        **forms
    )

@bot.route('/<Name>/delete', methods=['POST'])
@natural_to_surrogate_key(Bot_sql, 'Name')
def delete(Name, id):
    bot = Bot_sql.query.get_or_404(id)
    db.session.delete(bot)
    db.session.commit()
    flash(f'Bot has been deleted', 'success')
    return redirect(url_for('.list'))