from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from logIn import logIn
from db import login
from config import Config
from main import Main
from navegacion import Nav
from tienda import Tienda
from stats import Stats
from anyadir import anyadir
from eliminar import eliminar
app = Flask(__name__)
app.config.from_object(Config)

# app.register_blueprint(inicio, url_prefix="/inicio")
app.register_blueprint(logIn, url_prefix="/")
app.register_blueprint(Main, url_prefix="/")
app.register_blueprint(Nav, url_prefix="/")
app.register_blueprint(Tienda, url_prefix="/")
app.register_blueprint(Stats, url_prefix="/")
app.register_blueprint(anyadir, url_prefix="/")
app.register_blueprint(eliminar, url_prefix="/")

login.init_app(app)
login.login_view = 'login'
db_name = 'base.db'
db = SQLAlchemy()
db.init_app(app)

bootstrap = Bootstrap(app)
app.secret_key = (Config.SECRET_KEY)

"""
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
"""
