from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from inicio import inicio
from logIn import logIn
from db import Usuarios
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# app.register_blueprint(inicio, url_prefix="/inicio")
app.register_blueprint(logIn, url_prefix="/")

db_name = 'base.db'
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    try:
        usuarios = Usuarios.query.order_by(Usuarios.nombre).all()
        usuarios_name = '<ul>'
        for usuario in usuarios:
            usuarios_name += '<li>' + usuario.nombre + ', ' + usuario.direccion + '</li>'
        usuarios_name += '</ul>'
        return usuarios_name
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
