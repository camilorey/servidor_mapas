from flask import Blueprint

#configuración del blueprint para la página web
website = Blueprint('website',__name__,
                    static_folder='static',
                    template_folder='templates')
'''
El blueprint que tendrá la website que acompañará al
mapa. 
'''

#importamos todos los métodos para hacer un solo import aquí
from . import metodos_website
