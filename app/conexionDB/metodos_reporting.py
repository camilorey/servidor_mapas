from .members import Municipio

def get_lista_municipios():
    municipios = Municipio.filter(True).all()
    return municipios