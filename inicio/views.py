from flask import Blueprint, render_template

inicio = Blueprint(
            'inicio',
            __name__,
            template_folder="templates",
            static_folder='static'
        )
@inicio.route("/inicio")
def hello2_view():
    textoInicial = "Pagina de inicio"
    return render_template("inicio/inicio.html", greeting=greeting)