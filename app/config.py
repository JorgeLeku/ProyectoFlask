"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DEBUG = False
    TESTING = False
    # SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    SQLALCHEMY_DATABASE_URI = 'postgres://ifqlvinjywonwc:984d006e53da481e436e6d84420c2f107ca1ba94e25046653759fbf0de614d5d@ec2-18-203-62-227.eu-west-1.compute.amazonaws.com:5432/dbreehkc5m52u5'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
