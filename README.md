## Construyendo una sala de chat en tiempo real con Flask y SocketIO 🐍

###### Construye una sala de chat en tiempo real utilizando Flask y SocketIO. Esta poderosa combinación te permite crear una aplicación web interactiva con capacidades de chat en tiempo real. Flask te proporciona un marco web sólido y SocketIO facilita la comunicación bidireccional entre el servidor y el cliente para una experiencia de chat fluida

##### Paquetes necesarios

`pip install flask`
`pip install mysql-connector-python`
`pip install flask-socketio`

##### Generar archivo requirement.txt

`pip freeze > requirements.txt`

##### Instalar todos los paquetes del proyecto

`pip install -r requirements.txt`

#### Flask-Sockets es una extensión de Flask que proporciona una integración directa con el paquete WebSocket de Python, lo que te permite utilizar WebSocket en tu aplicación Flask. Puedes instalarlo utilizando pip: pip install Flask-Sockets.

### Nota

Puedes crear un entorno virtual con `virtualenv env` e instalar todos los paquetes del proyecto ejecutando ``pip install -r requirements.txt`
obvio cambiar los parametros para la conexión a BD e importar la tabla que se requiere para almacenar los mensajes de la sala de chat.

##### broadcast=True

Se utiliza al emitir un evento desde el servidor para especificar
que dicho evento debe ser transmitido a todos los clientes conectados,
excepto al cliente que generó el evento.

##### json.dumps()

Para convertir la lista de diccionarios en una cadena JSON
data_msj = json.dumps(respuesta_procesar_form) # Convertir a JSON
print(data_msj)

##### Documentación

https://flask-socketio.readthedocs.io/en/latest/index.html

### Resultado Final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/portada_flask-socketio__chat_urian_viera.PNG)

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/portada_flask_socketio_urian_viera.PNG)

# ¡Por favor, no olvides dejar tu comentario y darle like al canal! 👍 Además, si aún no lo has hecho, ¡te invito a suscribirte! 😀
