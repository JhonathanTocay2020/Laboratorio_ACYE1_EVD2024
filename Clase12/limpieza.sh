#!bin/bash

#Verificamos el nombre del archivo

if [ $# -ne 1 ]; then
	echo "Uso: $0 <nombre_archivo>"
	exit 1
fi

nombre_base="$1"

#Archivos a Limpiar

archivo_objeto="${nombre_base}.o"
archivo_ejecutable="${nombre_base}"

#Eliminar archivo Objeto
if [ -f"$archivo_objeto" ]; then
	echo "Eliminar el archivo objeto: $archivo_objeto"
	rm "$archivo_objeto"
else
	echo "No se ha encontrado el Archivo: $archivo_objeto"
fi

#Eliminar el Ejecutable

if [ -f"$archivo_ejecutable" ]; then
	echo "Eliminando el archivo ejecutable: $archivo_ejecutable"
	rm "$archivo_ejecutable"
fi

echo "Limpieza Completada"
