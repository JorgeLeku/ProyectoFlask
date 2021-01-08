
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

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
    id_usuario = db.Column(db.Integer, ForeignKey('usuarios.id'))
    id_productos = db.Column(db.Integer, ForeignKey("productos.id"))
    estado = db.Column(db.String)
    fechacreacion = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)


class Productos(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    categoria = db.Column(db.String)
    precio = db.Column(db.Numeric)
    ubicacion = db.Column(db.String)
    cantidad = db.Column(db.Integer)
