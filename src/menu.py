import util
import conf
if conf.reportarImportaciones: print("menu.py IMPORTADO")

estado = "inicio"

menuInicioEnum = {
	"consultar": 1,
	"consignar": 2,
	"retirar": 3,
	"clave": 4,
	"salir": 5
}

def menuInicio():
	print(f'{util.colorear("Menu principal:", "negrita", "subrayado", "verde")}')
	print("1. Consultar")
	print("2. Consignar")
	print("3. Retirar")
	print("3. Cambiar clave")
	print("")
	seleccion = int(input("Seleccione (1/4): "))

def iniciar():
	pass

def actualizar():
	if estado == "inicio":
		return menuInicio()
	return estado

def cerrar():
	pass