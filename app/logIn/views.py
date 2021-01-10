from flask import (Blueprint, render_template, request, redirect, session)
from flask_login import current_user, login_user
from db import Usuarios, db


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
