from app import create_app
from flask_ngrok import run_with_ngrok

RUN_TYPE = 'LOCAL'
'''
El tipo de run que queremos. 
    LOCAL: con el servidor local sin NGROK
    NGROK: usando un tunel NGROK para compartir
'''
#creamos una instancia de la app
servidor_mapas = create_app()

if RUN_TYPE == 'LOCAL':
    #ponemos a correr la app
    servidor_mapas.run(port=6666)
else:
    #envolvemos esto con ngrok
    run_with_ngrok(servidor_mapas)
    #ponemos a correr la app en una URL generada por NGROK
    servidor_mapas.run()
