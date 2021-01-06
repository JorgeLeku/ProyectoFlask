
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager
"""
import sqlite3
from flask import g, current_app
from flask.cli import with_appcontext"""

"""Intento con SQLAlchemy que daba error de compatiblilidad con Heroku y postgresql"""

db = SQLAlchemy()
login = LoginManager()


class Usuarios(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    direccion = db.Column(db.String)
    email = db.Column(db.String)
    numero = db.Column(db.String)
    password = db.Column(db.String)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))


class Pedidos(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    estado = db.Column(db.String)
    fechaCreacion = db.Column(db.DateTime)


class Productos(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    categoria = db.Column(db.String)
    precio = db.Column(db.Integer)
    ubicacion = db.Column(db.String)
    cantidad = db.Column(db.Integer)


class PedidoProductos(db.Model):
    __tablename__ = 'pedido_productos'
    id = db.Column(db.Integer, primary_key=True)
    id_productos = db.Column(db.Integer)
    id_pedidos = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)


"""def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@with_appcontext
def init_db_command():
    init_db()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
"""
