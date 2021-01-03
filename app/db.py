
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    creacion = db.Column(db.String)
    direccion = db.Column(db.String)
    email = db.Column(db.String)
    numero = db.Column(db.Integer)


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
    precio = db.Column(db.Numeric)
    ubicacion = db.Column(db.String)


class PedidoProductos(db.Model):
    __tablename__ = 'pedido_productos'
    id = db.Column(db.Integer, primary_key=True)
    id_productos = db.Column(db.Integer)
    id_pedidos = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
