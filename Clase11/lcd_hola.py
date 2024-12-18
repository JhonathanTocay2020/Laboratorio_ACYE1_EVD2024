from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

lcd.write_string("Hola Arqui1")

time.sleep(2)

lcd.clear()

lcd.write_string("Clase 11")

time.sleep(5)

lcd.clear()
