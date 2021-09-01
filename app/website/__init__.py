from flask import Blueprint

#configuración del blueprint para la página web
print("creando el blueprint del website")
website = Blueprint('website',__name__,
                    static_folder='static',
                    template_folder='templates')

#importamos todos los métodos para hacer un solo import aquí
from . import metodos_website
