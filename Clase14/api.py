from flask import Flask, jsonify
import adafruit_dht
import board
import time

SENSOR = adafruit_dht.DHT11(board.D4) #GPIO4

app = Flask(__name__)

@app.route('/sensor', methods=['GET'])
def capturar():
	try: 
		temperatura = SENSOR.temperature
		humedad = SENSOR.humidity
		
		if temperatura is not None and humedad is not None:
			return jsonify({
				"temperatura": round(temperatura, 1),
				"humedad": round(humedad, 1)
			})
		else: 
			return jsonify({
				"error": "Error al leer el Sensor",
			}), 500
	except Exception as e:
		return jsonify({"error": str(e)}), 500
		
if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=5000)
	except KeyboardInterrupt:
		print("Servidor detenido")
	finally:
		SENSOR.exit()