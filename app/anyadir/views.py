from flask import (Blueprint, render_template, request, flash)
from app.db import Productos, db
from flask_login import login_required


anyadir = Blueprint(
            'anyadir',
            __name__,
            template_folder="app/templates",
            static_folder='static'
        )


@anyadir.route("/anadirProducto", methods=['GET', 'POST'])
@login_required
def add_prod():
    if request.method == 'POST':
        if not request.form['nombre'] or not request.form['categoria'] or not request.form['ubicacion'] or not request.form['cantidad'] or not request.form['precio']:
            flash('Introduzca todos los datos', 'error')
        else:
            nombre = request.form['nombre']
            categoria = request.form['categoria']
            ubicacion = request.form['ubicacion']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            producto = Productos(nombre=nombre, categoria=categoria, ubicacion=ubicacion, cantidad=cantidad, precio=precio)
        db.session.add(producto)
        db.session.commit()
        flash('producto correctamente añadido')
        return('dasds')
    return render_template("anyadirProducto.html")
