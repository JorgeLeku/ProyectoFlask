from flask import (Blueprint, render_template, request, flash)
from app.db import Productos, db
import sys
anyadir = Blueprint(
            'anyadir',
            __name__,
            template_folder="templates",
            static_folder='static'
        )


@anyadir.route("/anadirProd", methods=['GET', 'POST'])
def add_prod():
    if request.method == 'POST':
        print("aaaaa")
        if not request.form['nombre'] or not request.form['categoria'] or not request.form['ubicacion'] or not request.form['cantidad'] or not request.form['precio']:
            flash('Introduzca todos los datos', 'error')
        else:
            producto = Productos(request.form['nombre'], request.form['categoria'], request.form['ubicacion'], request.form['cantidad'], request.form['precio'])
        db.session.add(producto)
        db.session.commit()
        flash('producto correctamente añadido')
        return('dasds')
    return render_template("anyadirProducto.html")
