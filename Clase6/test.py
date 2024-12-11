import mysql.connector

# Configuracion de la base de datos MySQL
DB_CONFIG = {
    'host': '192.168.1.13',  # Direccion IP del servidor MySQL
    'user': 'root',           # Usuario de MySQL
    'password': 'mysql1234',  # Contra de MySQL
    'database': 'data_arqui1' # Nombre de la base de datos
}

try:
    # Establecer la conexion
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Conexion exitosa a la base de datos MySQL")
    
    # Crear un cursor
    cursor = conn.cursor()
    
    # Probar una consulta 
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"Conectado a la base de datos: {db_name[0]}")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexion cerrada.")
