print("data.py IMPORTADO")
import data

def iniciarSesion(nombre, clave):
	#Nos aseguramos de tener los datos al dia
	data.cargarDatos()

	#Tomamos una copia de los datos
	datos = data.conseguirDatos()

	#Buscamos el usuario y confirmamos que
	#La clave sea la correcta
	for usuario in datos:
		if usuario["user"] == nombre and usuario["pass"] == clave:
			return True
	return False

def cambiarClave(nombre, claveAntigua, claveNueva):
	#Nos aseguramos de tener los datos al dia
	data.cargarDatos()

	#Tomamos una copia de los datos
	datos = data.conseguirDatos()

	#Buscamos el usuario y confirmamos que
	#La clave sea la correcta
	for usuario in datos:
		if usuario["user"] == nombre and usuario["pass"] == claveAntigua:
			usuario["pass"] == claveNueva
			return True
	return False

def bloquearUsuario()
