from flask import (Blueprint, render_template)

Nav = Blueprint(
            'Nav',
            __name__,
            template_folder="app/templates",
        )


@Nav.route("/barra")
def main():
    return render_template("navegacion.html")


@Nav.route('/inicio')
def view_home():
    return render_template("inicio.html", title="Inicio")


@Nav.route("/nada")
def view_first_page():
    return render_template("inicio.html", title="Stats")


@Nav.route("/login")
def view_second_page():
    return render_template("logIn.html", title="Login")
