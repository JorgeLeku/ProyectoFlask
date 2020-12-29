from flask import (Blueprint, render_template, request, redirect, session, url_for, flash)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
user = {"username": "abc", "password": "xyz"}
db = SQLAlchemy()
logIn = Blueprint(
            'logIn',
            __name__,
            template_folder="templates",
            static_folder='static'
        )


@logIn.route("/login", methods=['POST', 'GET'])
def inicio_view():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/dashboard')
        return "<h1>Wrong username or password</h1>"
    return render_template("logIn//logIn.html")


@logIn.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return '<h1>Welcome to the dashboard</h1>'

    return '<h1>You are not logged in.</h1>'


@logIn.route('/logout')
def logout():
    session.pop('user')  # session.pop('user') help to remove the session from the browser
    return redirect('/login')


@logIn.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        error = None

        if not email:
            error = 'Introduzca un email.'
        elif not username:
            error = 'Introduzca un usuario.'
        elif not password:
            error = 'Introduzca una contraseña.'
        elif db.execute(
            'SELECT id FROM usuarios WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = 'El usuario {} ya está registrado.'.format(email)

        if error is None:
            db.execute(
                'INSERT INTO user (email, username, password) VALUES (?, ?, ?)',
                (email, username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('/register.html')