from flask import (Blueprint, render_template)

Nav = Blueprint(
            'Nav',
            __name__,
            template_folder="app/templates",
        )


@Nav.route('/')
def view_home():
    return render_template("inicio.html", title="Inicio")


@Nav.route("/first")
def view_first_page():
    return render_template("index.html", title="First page")


@Nav.route("/login")
def view_second_page():
    return render_template("logIn.html", title="Login")
