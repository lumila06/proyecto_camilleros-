from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from datetime import datetime
fecha_actual = datetime.now()


app = Flask(__name__)

# Configuración CORS para aceptar cualquier origen
CORS(app)

# Configuración de la base de datos
db_config = {
    'user': 'usuario1',
   'password': '1234',
    'host': '127.0.0.1',
    'database': 'gestion'
}

# Ruta para obtener todas las admisiones
@app.route('/admissions', methods=['GET'])
def get_all_admissions():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT nombre, apellido, sexo, dni, edad, codigo, ubicacion FROM admisiones")
        admissions = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(admissions), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Ruta para obtener los servicios
@app.route('/services', methods=['GET'])
def get_services():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT nombre FROM servicios")
        services = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(services), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Nueva ruta para asignar servicio
@app.route('/assign-service', methods=['POST', 'OPTIONS'])
def assign_service():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        query = """
        INSERT INTO requerimientos (nombre, apellido, sexo, dni, edad, codigo, ubicacion, servicio, medio_transporte, solicitante) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['nombre'], 
            data['apellido'], 
            data['sexo'], 
            data['dni'], 
            data['edad'], 
            data['codigo'], 
            data['ubicacion'], 
            data['servicio'], 
            data['medio_transporte'], 
            data['solicitante']
        )

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"message": "Servicio asignado con éxito"}), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
