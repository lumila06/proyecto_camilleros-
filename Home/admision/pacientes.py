import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Habilita CORS en toda la aplicación Flask
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuración de la base de datos
db_config = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'user': os.getenv('DB_USER', 'usuario1'),
    'password': os.getenv('DB_PASS', '1234'),
    'database': os.getenv('DB_NAME', 'gestion')
}

# Función para conectar a la base de datos
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Conexión a la base de datos exitosa")
        return conn
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None

# Endpoint para verificar conexión a la base de datos
@app.route('/test-db', methods=['GET'])
def test_db_connection():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"message": "Conexión a la base de datos exitosa"}), 200
    else:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

# Endpoint para obtener todas las tareas con su estado
@app.route('/tareas', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT id, requerimiento_id, inicio_busqueda, inicio_traslado, 
                                 fin_traslado, ubicacion, medio_transporte, estado, nombre, 
                                 apellido, edad, servicio 
                          FROM tareas""")
        tasks = cursor.fetchall()
        print("Tareas obtenidas desde la base de datos:", tasks)  # Log para depuración
        return jsonify(tasks), 200
    except Error as e:
        print(f"Error al ejecutar la consulta SQL: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
