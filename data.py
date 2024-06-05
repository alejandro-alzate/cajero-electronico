"""
data.py
Objectivo:
Carga el archivo de inicio de sesion en memoria.

Interfaz:
cargarDatos():None
Lee el archivo (en este caso login.json) y lo carga a memoria internamente.

guardarDatos():None
Lee el los datos en memoria y los guarda al archivo.

conseguirDatos():Array
Retorna los datos cargados en memoria

establecerDatos(Array: nuevosDatos):None
Establece los datos dados por el parametro nuevosDatos
"""
import util
import json

data = []
config = {
	"path": "storage/login.json",
	"name": "login"
}

def cargarDatos():
	try:
		contenido = util.leerArchivoCompleto(config["path"])
		global data
		data = json.loads(contenido)
	except Exception as e:
		return e
	else:
		return True

def guardarDatos():
	try:
		util.escribirArchivoCompleto(config["path"], json.dumps(data))
	except Exception as e:
		return e
	else:
		return True

def conseguirDatos():
	return data

def establecerDatos(contenido):
	#global data
	#data = contenido
	print("esta funcion esta deshabilitada")
