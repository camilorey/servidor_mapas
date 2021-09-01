from .models import db

class Departamento(db.Model):
    '''
    La clase que va a representar los departamentos del país
    '''
    __tablename__ = "departamento"
    id = db.Column(db.String,primary_key=True)
    nombre = db.Column(db.String,nullable=False)

    def __init__(self,id,nombre):
        '''
        Constructor de la clase Departamento.
        :param id: el id del departamento como String
        :param nombre: Nombre del departamento como va a quedar
        '''
        self.id = id
        self.nombre = nombre

class Provincia(db.Model):
    '''
    La clase que va a representar las provincias del país
    '''
    __tablename__ = "provincia"
    id = db.Column(db.String,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    depto_id = db.Column(db.String,db.ForeignKey('departamento.id'))

    def __init__(self,id,nombre,depto_id):
        '''
        Constructor de la provincia
        :param id: el id de la provincia que vamos a usar
        :param nombre: el nombre de la provincia
        :param depto_id: el id del departamento al cual pertenece la provincia
        '''
        self.id = id
        self.nombre = nombre
        self.depto_id = depto_id

class Municipio(db.Model):
    '''
    La clase que va a representar el municipio.
    '''
    __tablename__ = "municipio"
    id = db.Column(db.String,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    depto_id = db.Column(db.String,db.ForeignKey('departamento.id'),
                         nullable=False)
    #vamos a agregar las provincias pero esto puede ser opcional
    provincia_id = db.Column(db.String,db.ForeignKey('provincia.id'),
                             nullable=True)

    def __init__(self,id,nombre,depto_id,provincia_id=None):
        '''
        Constructor del Municipio.
        :param id: id del municipio (Código DANE)
        :param nombre: nombre del municipio
        :param depto_id: el id del departamento al cual pertenece
        :param provincia_id: id de la provincia al cual pertenece (opcional)
        '''
        self.id = id
        self.nombre = nombre
        self.depto_id = depto_id
        if provincia_id is not None:
            self.provincia_id = provincia_id

class CentroPoblado(db.Model):
    '''
    La clase que va a representar el centro poblado
    '''
    __tablename__ = 'centro_poblado'
    id = db.Column(db.String,primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    tipo = db.Column(db.String,nullable=False)
    latitud = db.Column(db.Float,nullable=False)
    longitud = db.Column(db.Float,nullable=False)
    municipio_id = db.Column(db.String,db.ForeignKey('municipio.id'),
                             nullable=False)

    def __init__(self,id,nombre,tipo,lat,lon,municipio_id):
        '''
        El constructor del Centro poblado
        :param id: id del centro poblado (Código DANE)
        :param nombre: nombre del centro poblado
        :param tipo: CM si es cabecera municipal CP si no
        :param lat: latitud del centro poblado
        :param lon: longitud del centro poblado
        :param municipio_id: id del municipio al cual pertenece
        '''
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.latitud = lat
        self.longitud = lon
        self.municipio_id = municipio_id
