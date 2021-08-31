'''
Configuraciones de Flask para esta App
'''

from os import environ,path
from dotenv import load_dotenv

#Usamos el dotenv para cuadrar algunos parámetros de esta aplicación
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

class AppConfig:
    '''
    Esta clase va a tener las configuraciones básicas de la app
    '''
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

class DevConfig(AppConfig):
    '''
    Esta clase extiende App Config y agrega unas configuraciones
    adicionales para desarrollo.
    '''
    FLASK_ENV = 'DEVELOPMENT'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')

class ProdConfig(AppConfig):
    FLASK_ENV = 'PRODUCTION'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


