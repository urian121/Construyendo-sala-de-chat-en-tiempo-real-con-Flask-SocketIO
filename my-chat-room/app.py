from flask import Flask, render_template
# Importando las clases SocketIO y emit del módulo flask_socketio
from flask_socketio import SocketIO, emit

from funciones import *  # Importando mis Funciones


app = Flask(__name__)

# para crear una instancia de Socket.IO en una aplicación Flask
socketio = SocketIO(app)


# Escuchando si el servidor esta conectado del lado del servidor
@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')


# Escuchando si el cliente se desconecta del lado del servidor
@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')


# Definiendo mi ruta de Inicio
@app.route('/')
def index():
    lista_mensajes = lista_mensajes_chat() or []
    return render_template('public/inicio.html', lista_mensajes=lista_mensajes)


''' 
La función recibirMsj se encarga de escuchar el evento "message"
en el lado del servidor y mostrar el mensaje recibido en la consola del servidor.
'''


@socketio.on('mensaje_chat')
def recibir_mensaje(mensaje_chat):
    # print('Recibiendo mensaje: ' + mensaje_chat)
    respuesta_procesar_form = procesar_form_chat(mensaje_chat)
    """ 
    Emitiendo el resultado del template mensajes_chat.html directamente al cliente en lugar de convertirlo a JSON o una respuesta en particular
    """
    emit('mensaje_chat', render_template('public/mensajes_chat.html',
         lista_mensajes=respuesta_procesar_form), broadcast=True)


# Arrancando aplicacion Flask
if __name__ == '__main__':
    """ 
    se llama a la función socketio.run() para iniciar el servidor de Flask-SocketIO.
    Esto significa que cuando ejecutes este archivo específico, el servidor Flask-SocketIO 
    se iniciará y estará listo para recibir conexiones y manejar eventos de socket
    """
    socketio.run(app, debug=True, port=5100)
