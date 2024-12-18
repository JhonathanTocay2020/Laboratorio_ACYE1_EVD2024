from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)
mensaje = "Hola Curso Arquitectura de Computadoras 1"

# Desplazamiento hacia la izquierda

def texto_izquierda(lcd, texto, delay = 0.3):
	lcd.clear()
	texto_lenght = len(texto)
	
	for i in range(texto_lenght - 15):
		lcd.clear()
		lcd.write_string(texto[i: i + 16])
		time.sleep(delay)

def texto_derecha(lcd, texto, delay = 0.3):
	lcd.clear()
	texto_lenght = ""*16 + texto
	
	for i in range(len(texto_lenght) -15):
		lcd.clear()
		lcd.write_string(texto_lenght[-( i + 16):])
		time.sleep(delay)
		
#texto_izquierda(lcd, mensaje)
texto_derecha(lcd, mensaje)
lcd.clear()