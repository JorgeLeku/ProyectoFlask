from flask import (Blueprint, render_template)

Nav = Blueprint(
            'Nav',
            __name__,
            template_folder="app/templates",
        )


@Nav.route('/inicio')
def preview():
    return render_template("inicio.html", title="Inicio")


@Nav.route('/inicio')
def usuarios():
    return render_template("inicio.html", title="Inicio")


@Nav.route("/login")
def view_second_page():
    return render_template("logIn.html", title="Login")
