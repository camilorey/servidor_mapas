from app import create_app
from flask_ngrok import run_with_ngrok

RUN_TYPE = 'LOCAL'
'''
El tipo de run que queremos. 
    LOCAL: con el servidor local sin NGROK
    NGROK: usando un tunel NGROK para compartir
'''
#creamos una instancia de la app
app = create_app()

if RUN_TYPE == 'LOCAL':
    #ponemos a correr la app
    app.run()
else:
    #envolvemos esto con ngrok
    run_with_ngrok(app)
    #ponemos a correr la app en una URL generada por NGROK
    app.run()
