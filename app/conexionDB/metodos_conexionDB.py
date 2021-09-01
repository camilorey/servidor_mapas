from . import conexionDB
from .metodos_reporting import get_lista_municipios

@conexionDB.route('/')
def base():
    return "Este es el método base de esta sección"


@conexionDB.route('/lista_munis')
def lista_munis():
    lista_munis = get_lista_municipios()
    return lista_munis

