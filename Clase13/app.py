from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = {"status":"off"}

@app.route('/led', methods = ['GET'])
def get_led():
	return jsonify(led_state)
	
@app.route('/led', methods = ['POST'])
def encender():
	global led_state
	
	if not GPIO.getmode():
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(LED_PIN, GPIO.OUT)
		
	data = request.get_json()
	
	if "status" not in data:
		return jsonify({"error": "Agregue el parametro requerido"}), 400
		
	status = data["status"].lower()
	
	if status == "on":
		GPIO.output(LED_PIN, GPIO.HIGH)
		led_state["status"] = "on"
	elif status == "off":
		GPIO.output(LED_PIN, GPIO.LOW)
		led_state["status"] = "off"
	else:
		return jsonify({"error": "Ingrese un valor valido para el status"}), 400
	
	return(led_state)
	
@app.route('/led', methods = ['DELETE'])
def eliminar():
	GPIO.cleanup()
	led_state["status"] = "off"
	return jsonify({"msg": "Led apagada"}), 200
	
	
if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=5000)
	except KeyboardInterrupt:
		GPIO.cleanup()