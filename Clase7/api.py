from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
# Configuracion de la base de datos MySQL
DB_CONFIG = {
    'host': '35.245.48.76',  # Servidor MySQL
    'user': 'root',          # Usuario de MySQL
    'password': '<9E$"e9]k;ZqYm_k', # Contra de MySQL
    'database': 'clase6' # Nombre de tu base de datos
}

def get_last_data():
    """Funcion para obtener el ultimo dato insertado en la base de datos."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM dht11_data ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()  # Obtener el ultimo registro
    finally:
        cursor.close()
        conn.close()

    return result

@app.route('/datos', methods=['GET'])
def last_data():
    """Endpoint para obtener el ultimo dato insertado."""
    data = get_last_data()
    if data:
        return jsonify({
            'status': 'success',
            'data': data
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'No se encontraron datos en la base de datos.'
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
