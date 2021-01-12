from flask import (Blueprint, render_template)
from app.db import Usuarios, Productos, Pedidos
from sqlalchemy import func
from flask_login import login_required, current_user
Stats = Blueprint(
            'Stats',
            __name__,
            template_folder="app/templates",
        )


@Stats.route("/usuarios", methods=["GET"])
@login_required
def usuarios():
    usuarios = Usuarios.query.with_entities(Usuarios.email, Usuarios.nombre, Usuarios.direccion, Usuarios.numero).all()
    cantidad = Usuarios.query.with_entities(Usuarios.direccion, func.count(Usuarios.direccion)).group_by(Usuarios.direccion).all()
    return render_template("usuarios.html",  usuarios=usuarios, cantidades=cantidad, pedidos=pedidos)


@Stats.route("/almacenes", methods=["GET"])
@login_required
def almacenes():
    productos = Productos.query.all()
    cantidad = Productos.query.with_entities(Productos.ubicacion, func.count(Productos.ubicacion)).group_by(Productos.ubicacion).all()
    return render_template("almacenes.html",  productos=productos, pedidos=pedidos, cantidades=cantidad)


@Stats.route("/pedidos", methods=["GET"])
@login_required
def pedidos():
    pedidos = Usuarios.query.all()
    print(pedidos.nombre)
    return render_template("pedidos.html",  pedidos=pedidos)


@Stats.route("/stats")
@login_required
def stats():
    print("bbbbb")
    print(current_user)
    print("aaaaa")
    usuarios = Usuarios.query.with_entities(Usuarios.id, Usuarios.nombre, Usuarios.direccion).all()
    pedidos = Pedidos.query.all()
    productos = Productos.query.all()
    cnt_estado = Pedidos.query.with_entities(Pedidos.estado, func.count(Pedidos.estado)).group_by(Pedidos.estado).all()
    print(cnt_estado)
    cnt_productos = Pedidos.query.with_entities(Pedidos.id_productos, func.count(Pedidos.id_productos)).group_by(Pedidos.id_productos).all()
    cnt_usuarios = Pedidos.query.with_entities(Pedidos.id_usuario, func.count(Pedidos.id_usuario)).group_by(Pedidos.id_usuario).all()
    print(pedidos)
    return render_template("stats.html", cnt_usuarios=cnt_usuarios, cnt_productos=cnt_productos, cnt_estado=cnt_estado, usuarios=usuarios, pedidos=pedidos, productos=productos)
