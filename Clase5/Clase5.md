# Clase 5
### Instalacion de SO

### Conexion SSH
```cmd
ssh <USUARIO_RASPBERRY>@<IP_DE_LA_RASPBERRY>
```

Posterior al comando, se debe de agregar la contraseña.

### Instalar Neofetch

```cmd
# Actualizacion
sudo apt update && sudo apt upgrade -y  
# Instalar Neofetch 
sudo apt install neofetch -y            
# Probar
neofetch                                
```
# Ejemplo 1
```PYTHON
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:
  GPIO.output(7, True)
  time.sleep(1)
  GPIO.output(7, False)
  time.sleep(1)
```

## Crear Entorno Virtual

### 1. Crear un Entorno Virtual 

Instalar los paquetes en un entorno virtual 

1. Instalar las herramientas necesarias: Asegúrate de tener instalado python3-venv:
```ssh
sudo apt install python3-venv
```

2. Crear un entorno virtual:
```ssh
python3 -m venv ~/clase4
```

3. Activar el entorno virtual:
```ssh
source ~/clase4/bin/activate
```

4. Instalar adafruit-circuitpython-dht dentro del entorno: 
- Consideraciones: Instalar cuando este activado el entorno.
- Instala el paquete:

```ssh
pip install adafruit-circuitpython-dht
sudo apt install libgpiod2
```

