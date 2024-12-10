import adafruit_dht
import board

SENSOR = adafruit_dht.DHT11(board.D4)  

try:
    while True:
        # Leer los datos
        temperatura = SENSOR.temperature
        humedad = SENSOR.humidity

        # Verificar lectura
        if humedad is not None and temperatura is not None:
            print(f"Temperatura: {temperatura:.1f} C")
            print(f"Humedad: {humedad:.1f}%")
        else:
            print("Error al leer el sensor")
except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    SENSOR.exit()