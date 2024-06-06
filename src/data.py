"""
data.py
Objectivos:
Carga / Guarda el archivo de inicio de sesion en memoria.

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
print("data.py IMPORTADO")
import util
import json
import conf

data = []
config = {
	"path": "storage/login.json",
}

def cargarDatos():
	try:
		contenido = util.leerArchivoCompleto(conf.rutaBaseDeDatos)
		global data
		data = json.loads(contenido)
	except Exception as e:
		return e
	else:
		return True

def guardarDatos():
	try:
		util.escribirArchivoCompleto(conf.rutaBaseDeDatos, json.dumps(data))
	except Exception as e:
		return e
	else:
		return True

def conseguirDatos():
	return data

def establecerDatos(contenido):
	#global data
	#data = contenido
	print("esta funcion esta deshabilitada por el momento")
