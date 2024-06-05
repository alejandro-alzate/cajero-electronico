# Utilidades python
import platform
import os

def limpiarPantalla():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

#Todavia no se hace checkeo antes de leer o escribir archivos
def leerArchivoCompleto(archivo):
	with open(archivo) as file:
		content = file.read()
	return content

def escribirArchivoCompleto(archivo, datos):
	f = open(archivo, "")
	f.write(datos)
	f.close()