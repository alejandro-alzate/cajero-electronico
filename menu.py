print("menu.py IMPORTADO")
import util

estado = ""

def iniciar():
	print("menu.py INICIANDO")

def actualizar():
	if estado == "inicio":
		print("""
			Menu principal
			--------------
			1. Iniciar sesion
			2.
			""")
	return estado

def cerrar():
	pass