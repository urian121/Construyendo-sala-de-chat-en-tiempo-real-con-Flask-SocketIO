# Chat en Tiempo Real con Flask + SocketIO ⚡🐍

Sala de chat en tiempo real usando **Flask** y **SocketIO**, con comunicación bidireccional entre cliente y servidor.

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/portada_flask-socketio__chat_urian_viera.PNG)
![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/portada_flask_socketio_urian_viera.PNG)

## Instalación

### Paquetes necesarios

```bash
pip install flask flask-socketio mysql-connector-python
```

### Generar `requirements.txt`

```bash
pip freeze > requirements.txt
```

### Instalar dependencias del proyecto

```bash
pip install -r requirements.txt
```

### Entorno virtual (opcional)

```bash
virtualenv env
source env/bin/activate   # En Windows: env\Scripts\activate
```

## Notas importantes

* Configura los parámetros de conexión a tu base de datos.
* Importa la tabla donde se guardarán los mensajes.
* `broadcast=True`: envía el mensaje a todos los clientes excepto al emisor.
* `json.dumps()`: convierte listas/diccionarios a JSON para enviarlos al cliente.

## Documentación
[https://flask-socketio.readthedocs.io/en/latest/index.html](https://flask-socketio.readthedocs.io/en/latest/index.html)


## Apoya el proyecto ❤️

* Recomiéndalo 📢
* Invita una cerveza 🍺 o un café ☕
* PayPal: **[iamdeveloper86@gmail.com](mailto:iamdeveloper86@gmail.com)**
* ¡Suscríbete! 👍
