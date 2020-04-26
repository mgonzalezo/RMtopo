import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'key123'
#     #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#     #SQLALCHEMY_DATABASE_URI = 


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True