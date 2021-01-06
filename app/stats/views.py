from flask import (Blueprint, render_template)
from app.db import Usuarios, Productos, Pedidos
Stats = Blueprint(
            'Stats',
            __name__,
            template_folder="app/templates",
        )


@Stats.route("/usuarios", methods=["GET"])
def usuarios():
    usuarios = Usuarios.query.with_entities(Usuarios.email, Usuarios.nombre, Usuarios.direccion, Usuarios.numero).order_by(Usuarios.email).all()
    return render_template("usuarios.html",  usuarios=usuarios)


@Stats.route("/almacenes", methods=["POST"])
def almacenes(request):
    productos = Productos.query.with_entities(Productos.almacenes, Productos.nombre, Productos.categoria).all()
    return render_template("almacenes.html",  productos=productos)


@Stats.route("/pedidos", methods=["POST"])
def pedidos(request):
    pedidos = Pedidos.query.with_entities().all()
    return render_template("pedidos.html",  pedidos=pedidos)
