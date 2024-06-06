print("menu.py IMPORTADO")
import util

estado = ""

def menuInicio():
	print("""
		Menu principal
		--------------
		1. Iniciar sesion
		2. 
		""")
	input()

def iniciar():
	print("menu.py INICIANDO")

def actualizar():
	if estado == "inicio":
		menuInicio
	return estado

def cerrar():
	pass