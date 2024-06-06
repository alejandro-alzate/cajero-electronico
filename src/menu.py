import util
import conf
if conf.reportarImportaciones: print("menu.py IMPORTADO")

estado = "inicio"

menuEstadoEnum = {
	"consultar": 1,
	"retirar": 2,
	"consignar": 3,
	"clave": 4,
	"salir": 5
}

def menuInicio():
	print(f'{util.colorear("Menu principal:", "negrita", "subrayado", "verde")}')
	print("1. Consultar")
	print("2. Retirar")
	print("3. Consignar")
	print("4. Cambiar clave")
	print("5. Salir")
	seleccion = int(input("Seleccione (1/5): "))
	return seleccion

# def conseguirEstado():
# 	global estado
# 	return estado

def iniciar():
	pass

def actualizar():
	global estado
	if estado == "inicio":
		estado = menuInicio()
	return estado

def cerrar():
	pass