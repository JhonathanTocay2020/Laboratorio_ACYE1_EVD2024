import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sensor = 17
GPIO.setup(sensor, GPIO.IN)

try:
    while True:
        valor = GPIO.input(sensor)
        print(valor)
        
        if valor == GPIO.HIGH:
            print("Suelo seco")
        else:
            print("Suelo Humedo")
        
        time.sleep(1)
except KeyboardInterrpt:
    print("Fin del programa")
finally:
    GPIO.Cleanup()