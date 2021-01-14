from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.logIn import logIn
from app.db import login
from app.config import Config
from app.main import Main
from app.navegacion import Nav
from app.tienda import Tienda
from app.stats import Stats
from app.anyadir import anyadir
from app.eliminar import eliminar
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
