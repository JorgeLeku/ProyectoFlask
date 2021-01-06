from flask import (Blueprint, render_template, request, redirect, session)
from flask_login import current_user, login_user
from app.db import Usuarios, db


import sys
logIn = Blueprint(
            'logIn',
            __name__,
            template_folder="app/templates",
            static_folder='static'
        )


@logIn.route('/login', methods=['POST', 'GET'])
def log():
    if current_user.is_authenticated:
        return redirect('/inicio.html')
    if request.method == 'POST':
        email = request.form['email']
        user = Usuarios.query.filter_by(email=email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('inicio.html')
    return render_template('logIn.html')


@logIn.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/inicio')
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre']
        password = request.form['password']
        direccion = request.form['direccion']
        numero = request.form['telefono']
        if Usuarios.query.filter_by(email=email).first():
            usuarios = Usuarios.query.filter_by(email=email)
            usuarios_name = '<ul>'
            for usuario in usuarios:
                usuarios_name += '<li>' + usuario.nombre + ', ' + usuario.direccion + '</li>'
                usuarios_name += '</ul>'
            print(usuarios_name, file=sys.stdout)
            return ('Email already Present')
        user = Usuarios(email=email, nombre=nombre, numero=numero, direccion=direccion)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('registro.html')


@logIn.route('/logout')
def logout():
    session.pop('user')  # session.pop('user') help to remove the session from the browser
    return redirect('/login')


"""
@logIn.route('/regisster', methods=('GET', 'POST'))
def regsister():
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
"""

"""
import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db
# from app.db import Usuarios, db
logIn = Blueprint(
            'logIn',
            __name__,
            template_folder="app/templates",
            static_folder='static'
        )


@logIn.route('/registro', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        nombre = request.form['nombre']
        password = request.form['password']
        direccion = request.form['direccion']
        numero = request.form['telefono']
        db = get_db()
        error = None

        if not email:
            error = 'Introduzca email'
        elif not username:
            error = 'Introduzca usuario'
        elif not password:
            error = 'Introduzca contraseña'
        elif not nombre:
            error = 'Introduzca nombre'
        elif not direccion:
            error = 'Introduzca direccion'
        elif not numero:
            error = 'Introduz'
        elif db.execute(
            'SELECT id FROM usuarios WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = 'El usuario {} ya esta registrado'.format(email)

        if error is None:
            db.execute(
                'INSERT INTO usuarios (nombre, direccion, email, numero, password) VALUES (?, ?, ?, ?, ?)',
                (nombre, direccion, email, numero, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('/registro.html')


@logIn.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('/login.html')


@logIn.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@logIn.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
"""
