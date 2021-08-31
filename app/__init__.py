from flask import Flask
from . import config

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
    app.config.from_object(config.DevConfig)

    #configuración de producción (descomentar cuando sea apropiado)
    #app.config.from_object(config.ProdConfig)

    #-------------------espacio para declarar los blueprints----------
    # from .carpeta import <nom_paquete>
    # app.register_blueprint(<nom_paquete>,url_prefix='/<nom_url>')

    return app
