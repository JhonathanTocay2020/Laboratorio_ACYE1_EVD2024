from flask import Flask, jsonify, request
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

@app.route('/tiempo', methods=['GET'])
def control_tiempo():
	vartime = request.args.get('time', default = '5', type= str)
	
	if vartime == '5':
		print('Selecciono 5 segundos')
		return jsonify({
				"mensaje": "Selecciono 5 segundos",
		})
	elif vartime == '10':
		print('Selecciono 10 segundos')
		return jsonify({
				"mensaje": "Selecciono 10 segundos",
		})
	elif vartime == '15':
		print('Selecciono 15 segundos')
		return jsonify({
				"mensaje": "Selecciono 15 segundos",
		})
	elif vartime == '20':
		print('Selecciono 20 segundos')
		return jsonify({
				"mensaje": "Selecciono 20 segundos",
		})
	else:
		return jsonify({
				"error": "Error enviar los datos",
		}), 500
	
if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=5000)
	except KeyboardInterrupt:
		print("Servidor detenido")
	finally:
		SENSOR.exit()
