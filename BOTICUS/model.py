from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bot_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), unique=True, nullable=False)
    API_Key = db.Column(db.String(100), unique=True, nullable=False)
    Status = db.Column(db.Integer)
    Description = db.Column(db.Text)

"""
INIT DATABASE
"""

INIT_TABLES = [
 
]
INIT_DIRECTORY_NAME = "BOTICUS/db/initial"
TABLES_TO_SAVE = [
    Bot_sql
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