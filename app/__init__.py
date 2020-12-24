from flask import Flask
from app.inicio import inicio
#from app.configmodule import DevelopmentConfig
app = Flask(__name__)
app.config.from_object('app.config.DevelopmentConfig')
app.register_blueprint(inicio, url_prefix="/inicio")