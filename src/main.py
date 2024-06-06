"""
main.py
Objectivos:
Archivo maestro, este orquestra todos los recursos
"""

import data
import util
import menu
import cash
import session
import conf
if conf.reportarImportaciones: print("main.py INICIADO")


menu.iniciar()
menu.actualizar()

while True:
	print(menu.estado)
	if menu.estado == menu.menuEstadoEnum["salir"]:
		exit()
