"""
util.py
Utilidades de uso generico para uso comun

limpiarPantalla():None
limpia el contenido del terminal

leerArchivoCompleto(String archivo):String Contenido
Lee el archivo "archivo" y retorna su contenido

escribirArchivoCompleto(String archivo, String datos):None
Escribe el archivo "archivo" con el contenido dado en datos
"""
import platform
import os
config = {
	"modoLimpiarPantalla": "externo"
}


def limpiarPantalla():
	if config["modoLimpiarPantalla"] == "externo":
		if platform.system() == "Windows":
			os.system("cls")
		elif platform.system() == "Linux":
			os.system("clear")
	else:
		print("\033[2J")

#Todavia no se hace checkeo antes de leer o escribir archivos
def leerArchivoCompleto(archivo):
	with open(archivo) as file:
		content = file.read()
	return content

def escribirArchivoCompleto(archivo, datos):
	f = open(archivo, "")
	f.write(datos)
	f.close()