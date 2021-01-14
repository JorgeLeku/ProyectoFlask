from flask import (Blueprint, render_template, request, flash, redirect)
from app.db import (Productos, Pedidos, Usuarios, db)
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required

eliminar = Blueprint(
            'eliminar',
            __name__,
            template_folder="app/templates",
            static_folder='static'
        )
prodEliminado = ''


@eliminar.route("/eliminarPedido", methods=['GET', 'POST'])
@login_required
def rm_ped():
    if request.method == 'POST':
        if not request.form['id_pedido']:
            flash('Debe introducir un id de Pedido')
        else:
            idPedido = request.form['id_pedido']
            q = "DELETE FROM pedidos WHERE id=" + idPedido
            try:
                db.session.execute(q)
                db.session.commit()
            except SQLAlchemyError:
                flash('Error al eliminar Pedido')
            else:
                flash('Pedido eliminado')
        return redirect('/eliminarPedido')
    else:
        pedidos = Pedidos.query.all()
        usuarios = Usuarios.query.all()
        productos = Productos.query.all()
    return render_template("eliminarPedido.html", pedidos=pedidos, usuarios=usuarios, productos=productos)


@eliminar.route("/eliminarProducto", methods=['GET', 'POST'])
@login_required
def rm_prod():
    if request.method == 'POST':
        if not request.form['id_producto']:
            flash('Debe introducir un id de Producto')
        else:
            idProducto = request.form['id_producto']
            p = "DELETE FROM pedidos WHERE id_productos=" + idProducto
            q = "DELETE FROM productos WHERE id=" + idProducto
            try:
                db.session.execute(p)
                db.session.commit()
                db.session.execute(q)
                db.session.commit()
            except SQLAlchemyError:
                flash('Error al eliminar Producto')
            else:
                flash('Producto eliminado')
        return redirect('/eliminarProducto')
    else:
        productos = Productos.query.all()
    return render_template("eliminarProducto.html", productos=productos)
