from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class User_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

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