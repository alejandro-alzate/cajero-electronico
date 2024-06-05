"""
cash.py
Objectivo:
Consultar Retirar y/o Consignar dinero a un usuario
"""

import data


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


