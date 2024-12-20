#!bin/bash

if [ $# -ne 1 ]; then
    echo "Uso: $0 <archivo.s>"
    exit 1
fi

archivo_fuente="$1"
archivo_objeto="${archivo_fuente%.s}.o"
archivo_ejecutable="${archivo_fuente%.s}"

#Compilar
echo "Compilando $archivo_fuente..."
as -o "$archivo_objeto" "$archivo_fuente"

if [ $? -ne 0 ]; then
	echo "Error al compilar archivo"
	exit 1
fi

# Enlazar
echo "Enlazando $archivo_objeto..."
ld -o "$archivo_ejecutable" "$archivo_objeto"

if [ $? -ne 0 ]; then
	echo "Error al enlazar el archivo"
	exit 1
fi

#ejecutar
echo "Ejecutando $archivo_ejecutable ..."
./"$archivo_ejecutable"
resultado=$?

echo "Salida: $resultado"
