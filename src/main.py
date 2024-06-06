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

while True:
	estado = menu.actualizar()