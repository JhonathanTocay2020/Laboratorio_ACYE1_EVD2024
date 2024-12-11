import adafruit_dht
import board
import mysql.connector
import time

# Configuracion del sensor
SENSOR = adafruit_dht.DHT11(board.D4) 

# Configuracion de la base de datos MySQL
DB_CONFIG = {
    'host': '192.168.1.12',  #  servidor MySQL
    'user': 'root',             # Usuario de MySQL
    'password': 'mysql1234',      # contra de MySQL
    'database': 'data_arqui1'    # nombre de tu base de datos
}

# Conexion a la base de datos
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Crear tabla para los datos si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS dht11_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperatura FLOAT,
    humedad FLOAT
)
''')
conn.commit()  # Aplicar los cambios

try:
    while True:
        # Leer los datos del sensor
        temperatura = SENSOR.temperature
        humedad = SENSOR.humidity
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Formato de fecha y hora

        # Verificar si la lectura fue exitosa
        if humedad is not None and temperatura is not None:
            print(f"Temperatura: {temperatura:.1f} C")
            print(f"Humedad: {humedad:.1f}%")

            # Guardar los datos en la base de datos
            cursor.execute('''
                INSERT INTO dht11_data (timestamp, temperatura, humedad)
                VALUES (%s, %s, %s)
            ''', (timestamp, temperatura, humedad))
            conn.commit()  # Aplicar los cambios
        else:
            print("Error al leer el sensor")

        time.sleep(2)  # Esperar 2 segundos entre lecturas

except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    SENSOR.exit()
    cursor.close()
    conn.close()  # Cerrar la conexion a la base de datos
