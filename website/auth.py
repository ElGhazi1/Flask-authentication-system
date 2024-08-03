from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from . import mysql

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        name = data.get('name')
        password = data.get('password')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (name, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['username'] = user[1]
            return redirect(url_for('views.dashboard'))
        else:
            flash('Invalid username or password', category='error')
            return redirect(request.url)

    else:
        if 'username' in session:
            return redirect(url_for('views.dashboard'))
        return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        data = request.form
        username = data.get('name')
        pass1 = data.get('password1')
        pass2 = data.get('password2')

        if username is None or len(username) < 4:
            flash('Username should be greater than 4 characters', category='error')
        elif len(pass1) < 7:
            flash('Password should be greater than 7 characters', category='error')
        elif pass1 != pass2:
            flash('Passwords don\'t match', category='error')
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, pass1))
            mysql.connection.commit()
            cur.close()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('sign_up.html')
