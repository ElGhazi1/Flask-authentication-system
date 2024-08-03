from flask import Blueprint, render_template, current_app, g
from . import mysql

views = Blueprint('views', __name__)


@views.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    cur.close()
    return render_template('home.html',data=str(data))

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/privacy')
def privacy():
    return render_template('privacy.html')

@views.route('/dash')
def dashboard():
    return render_template('dashboard.html')
