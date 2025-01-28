from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir todos los orígenes

# Configuración de la base de datos
db_config = {
    'user': 'usuario1',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'gestion'
}

# Manejo de solicitudes preflight (OPTIONS)
@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = response.headers

        # Agrega los encabezados necesarios para CORS
        headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'

        return response

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Backend is working"})

@app.route('/submit-admission', methods=['POST'])
def submit_admission():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insertar datos en la base de datos
        cursor.execute("""
            INSERT INTO admisiones (nombre, apellido, sexo, dni, edad, codigo, ubicacion)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (data.get('firstName'), data.get('lastName'), data.get('gender'), data.get('dni'), data.get('age'), data.get('code'), data.get('location')))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({"message": "Datos enviados correctamente"})
    
    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)