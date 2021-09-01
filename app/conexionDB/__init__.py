from flask import Blueprint

#configuración del blueprint que se conecta a la DB
print("creando Blueprint para conectarnos a la DB")
conexionDB = Blueprint('conexionDB',__name__,
                       static_folder='static',
                       template_folder='template')



#traemos todos los métodos del backend de la conexión
from  . import metodos_conexionDB