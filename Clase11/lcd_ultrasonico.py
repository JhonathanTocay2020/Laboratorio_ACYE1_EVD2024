import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

GPIO.setmode(GPIO.BCM)
TRIGGER = 23
ECHO = 24

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def medir():
	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)

	#Esperar al inicio del pulso
	while GPIO.input(ECHO) == 0:
		inicio = time.time()
	
	#Esperar a que el pulso termine
	while GPIO.input(ECHO) == 1:
		fin = time.time()
		
	#Calcular la duracion del pulso
	duracion = fin - inicio
	
	#Calcular distancia (cm)
	distancia = (duracion * 34000)/2
	return distancia
	
try:
	while True: 
		distancia = medir()
		print(f"Distancia: {distancia:.2f} cm")
		# Uso de LCD
		lcd.clear()
		lcd.write_string(f"Distancia: {distancia:.2f} cm")
		time.sleep(1)
		
except KeyboardInterrupt:
	print("Programa finalizado")
finally:
	GPIO.cleanup()
	lcd.clear()
	lcd.write_string("Programa Detenido")
	time.sleep(5)
	lcd.clean