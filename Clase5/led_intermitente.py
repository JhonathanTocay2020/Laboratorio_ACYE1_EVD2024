import RPi.GPIO as GPIO
import time

# Configuración del modo de numeración de pines
GPIO.setmode(GPIO.BCM)  # Usa numeración BCM (broadcom)

# Configurar el pin GPIO
LED_PIN = 20  # GPIO al que está conectado el LED
GPIO.setup(LED_PIN, GPIO.OUT)  # Configurarlo como salida

try:
    print("Presiona Ctrl+C para detener el programa")
    while True:
        print("Encendiendo el LED")
        GPIO.output(LED_PIN, GPIO.HIGH)  # Encender el LED
        time.sleep(3)  # Esperar 3 segundos
        print("Apagando el LED")
        GPIO.output(LED_PIN, GPIO.LOW)  # Apagar el LED
        time.sleep(3)  # Esperar 3 segundos
except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    GPIO.cleanup()  # Restablecer todos los pines GPIO