"""
util.py
Utilidades de uso generico para uso comun

limpiarPantalla():None
limpia el contenido del terminal

leerArchivoCompleto(String archivo):String Contenido
Lee el archivo "archivo" y retorna su contenido

escribirArchivoCompleto(String archivo, String datos):None
Escribe el archivo "archivo" con el contenido dado en datos
"""
import platform
import warnings
import conf
import os

if conf.reportarImportaciones: print("util.py IMPORTADO")

def limpiarPantalla():
	if conf.modoLimpiarPantalla == "externo":
		if platform.system() == "Windows":
			os.system("cls")
		elif platform.system() == "Linux":
			os.system("clear")
	elif conf.modoLimpiarPantalla == "interno":
		print("\033[2J")
	else:
		warnings.warn("""
			util.py METODO DE LIMPIEZA DESCONFIGURADO!
			Use 'interno' ó 'externo' en el parametro
			'modoLimpiarPantalla' en 'conf.py'
			""")


#Todavia no se hace checkeo antes de leer o escribir archivos
def leerArchivoCompleto(archivo):
	with open(archivo) as file:
		content = file.read()
	return content

def escribirArchivoCompleto(archivo, datos):
	f = open(archivo, "")
	f.write(datos)
	f.close()


colors = {
	"reset": [0, 0],

	"bold": [1, 22],
	"dim": [2, 22],
	"italic": [3, 23],
	"underline": [4, 24],
	"inverse": [7, 27],
	"hidden": [8, 28],
	"strikethrough": [9, 29],

	"black": [30, 39],
	"red": [31, 39],
	"green": [32, 39],
	"yellow": [33, 39],
	"blue": [34, 39],
	"magenta": [35, 39],
	"cyan": [36, 39],
	"white": [37, 39],
	"gray": [90, 39],
	"grey": [90, 39],

	"brightRed": [91, 39],
	"brightGreen": [92, 39],
	"brightYellow": [93, 39],
	"brightBlue": [94, 39],
	"brightMagenta": [95, 39],
	"brightCyan": [96, 39],
	"brightWhite": [97, 39],

	"bgBlack": [40, 49],
	"bgRed": [41, 49],
	"bgGreen": [42, 49],
	"bgYellow": [43, 49],
	"bgBlue": [44, 49],
	"bgMagenta": [45, 49],
	"bgCyan": [46, 49],
	"bgWhite": [47, 49],
	"bgGray": [100, 49],
	"bgGrey": [100, 49],

	"bgBrightRed": [101, 49],
	"bgBrightGreen": [102, 49],
	"bgBrightYellow": [103, 49],
	"bgBrightBlue": [104, 49],
	"bgBrightMagenta": [105, 49],
	"bgBrightCyan": [106, 49],
	"bgBrightWhite": [107, 49],
}

colores = {
	"reiniciar":				[	0,		0	],

	"negrita":					[	1,		22	],
	"tenue":					[	2,		22	],
	"cursiva":					[	3,		23	],
	"subrayado":				[	4,		24	],
	"inverso":					[	7,		27	],
	"oculto":					[	8,		28	],
	"tachado":					[	9,		29	],

	"negro":					[	30,		39	],
	"rojo":						[	31,		39	],
	"verde":					[	32,		39	],
	"amarillo":					[	33,		39	],
	"azul":						[	34,		39	],
	"magenta":					[	35,		39	],
	"cian":						[	36,		39	],
	"blanco":					[	37,		39	],
	"gris":						[	90,		39	],
	"grisClaro":				[	90,		39	],

	"rojoBrillante":			[	91,		39	],
	"verdeBrillante":			[	92,		39	],
	"amarilloBrillante":		[	93,		39	],
	"azulBrillante":			[	94,		39	],
	"magentaBrillante":			[	95,		39	],
	"cianBrillante":			[	96,		39	],
	"blancoBrillante":			[	97,		39	],

	"fondoNegro":				[	40,		49	],
	"fondoRojo":				[	41,		49	],
	"fondoVerde":				[	42,		49	],
	"fondoAmarillo":			[	43,		49	],
	"fondoAzul":				[	44,		49	],
	"fondoMagenta":				[	45,		49	],
	"fondoCian":				[	46,		49	],
	"fondoBlanco":				[	47,		49	],
	"fondoGris":				[	100,	49	],
	"fondoGrisClaro":			[	100,	49	],

	"fondoRojoBrillante":		[	101,	49	],
	"fondoVerdeBrillante":		[	102,	49	],
	"fondoAmarilloBrillante":	[	103,	49	],
	"fondoAzulBrillante":		[	104,	49	],
	"fondoMagentaBrillante":	[	105,	49	],
	"fondoCianBrillante":		[	106,	49	],
	"fondoBlancoBrillante":		[	107,	49	],
}

def colorearSimple(texto, color):
	if color in colores:
		abierto, cerrado = colores[color]
		string = "\033[{0}m{1}\033[{2}m"
		return string.format(str(abierto), texto, str(cerrado))
		#return f"\033[{abierto}m{texto}\033[{cerrado}m"#\033[0m"
	return texto


def colorear(texto, *colores_modificadores):
	secuencias_abrir = []
	secuencias_cerrar = []

	for color in colores_modificadores:
		if color in colores:
			abrir, cerrar = colores[color]
			secuencias_abrir.append(f"\x1b[{abrir}m")
			secuencias_cerrar.insert(0, f"\x1b[{cerrar}m")  # Añadir al inicio para cerrar en orden inverso

	secuencia_abrir = "".join(secuencias_abrir)
	secuencia_cerrar = "".join(secuencias_cerrar)
	
	return f"{secuencia_abrir}{texto}{secuencia_cerrar}"