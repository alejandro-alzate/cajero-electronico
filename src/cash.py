"""
cash.py
Objectivo:
Consultar Retirar y/o Consignar dinero a un usuario
"""
import data
import conf
if conf.reportarImportaciones: print("cash.py IMPORTADO")

def consultarSaldo(nombre):
	#Nos aseguramos de tener los datos al dia
	data.cargarDatos()

	#Tomamos una copia de los datos
	datos = data.conseguirDatos()

	#Buscamos el usuario y retornamos el saldo
	for usuario in datos:
		if usuario["user"] == nombre:
			return usuario["cash"]
	return False

def cambiarSaldo(usuario, monto):
	#Nos aseguramos de tener los datos al dia
	data.cargarDatos()

	#Tomamos una copia de los datos
	datos = data.conseguirDatos()

	#Buscamos el usuario y cambiamos el valor y
	#retornamos el saldo nuevo.
	for usuario in datos:
		if usuario["user"] == nombre:
			usuario["cash"] = usuario["cash"] + monto
			return usuario["cash"]
	return False

