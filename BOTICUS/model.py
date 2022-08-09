from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import UserMixin

db = SQLAlchemy()

class User_sql(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self): # pragma: no cover
        return f"User('{self.id}','{self.username}','{self.email}', '{self.password}')"

import csv
from BOTICUS.login import hash_generate

class Bots_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    api_key = db.Column(db.String(100), unique=True)
    status = db.Column(db.Integer)

class Channels_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channelid = db.Column(db.Integer)


"""
INIT DATABASE
"""
### uncomment out below for table with prepopulated data

INIT_TABLES = [
    User_sql
]
INIT_DIRECTORY_NAME = "BOTICUS/db/initial"
TABLES_TO_SAVE = [
    Bots_sql,
    Channels_sql
]
TABLE_ROW_PROCESS = {
    User_sql: { 'password': hash_generate },
}

def create_db():
    try: db.drop_all()
    except: pass
    db.create_all()
    import csv
    import os
    for table in INIT_TABLES:
        filename = table.__name__ + '.csv'
        filename = os.path.join(INIT_DIRECTORY_NAME, filename)
        with open(filename, newline='') as file:
            for row in csv.DictReader(file):
                db.session.add(table(**row))
    db.session.commit()

def table_to_csv_file(table, file):
    from sqlalchemy_csv_normalise import denormalise_prepare
    q, col_names = denormalise_prepare(db.session, table)
    csv_file_writer = csv.writer(file)
    csv_file_writer.writerow(col_names)
    csv_file_writer.writerows(q.all())

def _date_interpret(table):
    # Interpret 'now+2' as 2 hours ahead, 'now-3.5' as 3.5 hours ago
    from datetime import datetime, timedelta
    from flask_sqlalchemy import inspect
    coerceables = {}
    def _string_to_date(s):
        if not s.startswith("now"):
            return s
        hour_delta = float(s[3:])
        return datetime.now() + timedelta(hours=hour_delta)
    for c in inspect(table).columns:
        if c.type.python_type == datetime:
            coerceables[c.name] = _string_to_date
    def _row_coercer(d):
        c = dict(d)
        for col in c:
            if isinstance(c[col], str) and coerceables.get(col, False):
                c[col] = coerceables[col](c[col])
        return c
    return _row_coercer

def csv_file_to_table(table, file, delete_first=False):
    from sqlalchemy_csv_normalise import renormalise_prepare, empty_deleter,\
        type_coercer
    row_maker = renormalise_prepare(db.session, table)
    row_cleaner = empty_deleter(table)
    row_coercer = type_coercer(table)
    row_date_munger = _date_interpret(table)
    row_postprocess = TABLE_ROW_PROCESS.get(table, lambda x: x)
    if isinstance(row_postprocess, dict):
        row_postprocess = lambda r, row_postprocess=row_postprocess: {
            k: row_postprocess.get(k, lambda x: x)(v)
                for k, v in r.items()
        }
    if delete_first: # pragma: no cover
        db.session.query(table).delete()
    for d in csv.DictReader(file):
        clean_row = row_cleaner(row_maker(d))
        row = row_postprocess(row_coercer(row_date_munger(clean_row)))
        db.session.add(table(**row))
    db.session.commit()