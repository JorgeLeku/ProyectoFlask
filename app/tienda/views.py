from flask import (Blueprint, render_template, request)
from db import Productos
from flask_login import current_user
Tienda = Blueprint(
            'Tienda',
            __name__,
            template_folder="app/templates",
        )


@Tienda.route('/<path:path>.html', methods=['POST', 'GET'])
def page(producto):
    producto = request.form['producto']
    return render_template('producto.html', producto=producto)


@Tienda.route('/')
def index():
    productos = Productos.query.order_by(Productos.nombre).all()
    if 'prod' in request.form:
        print('aaaaaaaaaaa')
        producto = request.form['producto']
        return render_template('producto.html', producto=producto)
    return render_template('tienda.html', current_user=current_user, productos=productos)
