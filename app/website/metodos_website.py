from . import website
from flask import render_template
BASE_PATH = 'app/website/static/'
'''
Dirección para acceder a los assets de la página web
'''
@website.route('/')
def home():
    return render_template('home.html')