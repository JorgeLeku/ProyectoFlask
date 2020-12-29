from flask import Blueprint, render_template


inicio = Blueprint(
            'inicio',
            __name__,
            template_folder="templates",
            static_folder='static'
        )


@inicio.route("/")
def inicio_view():
    textoInicial = "Pagina de inicio"
    return render_template("inicio//inicio.html", textoInicial=textoInicial)
