from flask import current_app, g
from flask_mysqldb import MySQL

def get_db():
    if 'db' not in g:
        g.db = current_app.extensions['mysql'].connection.cursor()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
