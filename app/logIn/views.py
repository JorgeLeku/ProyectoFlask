from flask import (Blueprint, render_template, request, redirect, session, url_for, flash)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
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
        email = request.form.get('email')
        password = request.form.get('password')
        if not email:
            error = 'Introduzca el email'
        elif not password:
            error = 'Introduzca la contraseña'
        else:
            usuario = db.execute(
                'SELECT * FROM usuarios WHERE email = ?', (email,)
            ).fetchone()
            if usuario is None and not check_password_hash(usuario['password'], password):
                error = 'email o contraseña incorrectos'
            if error is None:
                session.clear()
                session['user_id'] = usuario['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template("logIn//logIn.html")


@logIn.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == usuario['username']):
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
