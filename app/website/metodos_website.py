from . import website
from flask import render_template


BASE_PATH = 'app/website/static/'
'''
Dirección para acceder a los assets de la página web
'''
@website.route('/')
def home():
    '''
    Método para desplegar el home de este servidor
    :return: template del Home.
    '''
    print('En el método de home del website')
    return render_template('home.html')