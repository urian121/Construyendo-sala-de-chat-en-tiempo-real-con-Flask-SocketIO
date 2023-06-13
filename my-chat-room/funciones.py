from confiBD.conexionBD import *


def lista_mensajes_chat():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = "SELECT *, DATE_FORMAT(fecha_mensaje, '%d-%m-%Y %I:%i %p') AS fecha_formateada FROM chat ORDER BY id_chat ASC"
                mycursor.execute(querySQL,)
                lista_chat = mycursor.fetchall()
                if lista_chat:
                    return lista_chat
                else:
                    return {}
    except Exception as e:
        print(f"Ocurrió un error listando los chat: {e}")
        return 0


def procesar_form_chat(mensaje):
    try:
        # Conexión a la base de datos
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                sql = (
                    "INSERT INTO chat(mensaje) VALUES (%s)")
                valores = (mensaje,)
                cursor.execute(sql, valores)
                conexion_MySQLdb.commit()

                resultado_insert = cursor.rowcount
                if (resultado_insert):
                    return lista_mensajes_chat()
                else:
                    return []
    # Simplemente se utiliza para capturar cualquier excepción que se produzca en el bloque try
    except Exception as e:
        return f'Se produjo un error al insertar registrar el mensaje: {str(e)}'
