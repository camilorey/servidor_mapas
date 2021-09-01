from flask import Flask
from . import config

#importamos cada uno de los blueprints
from .website import website
from .conexionDB import conexionDB
from .conexionDB.models import db

def create_app():
    '''
    Este método crea la app de Flask usando las configuraciones
    de los objetos creados antes.
    :return: app Flask con la configuración escogida
    '''

    #creamos la instancia de la aplicación
    app = Flask(__name__)

    #cargamos las configuraciones de esta aplicación en la aplicación
    #configuración de desarrollo
    print("aplicando configuración de desarrollo")
    app.config.from_object(config.DevConfig)

    #configuración de producción (descomentar cuando sea apropiado)
    #app.config.from_object(config.ProdConfig)

    #inicializamos la DB con las propiedades de la app
    # db.init_app(app)
    #with app.app_context():
    #    db.create_all()

    #-------------------espacio para declarar los blueprints----------

    #blueprint de la página web
    app.register_blueprint(website, url_prefix='/web')

    #blueprint que se va a encargar de la conexión a la DB
    app.register_blueprint(conexionDB,url_prefix='/conn')

    return app
