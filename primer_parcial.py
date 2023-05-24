import json
import csv
import re

def leer_json_dream_team(nombre_archivo: str, clave:str):
    '''
	# Esta funcion lee el archivo .json del Dream team, mas especificamente sobre la info de los jugadores.
    # Recibe por parametros la ruta del archivo .json y un string para acceder a los jugadores
    # Retorna una lista de diccionarios con los datos de los jugadores.
    '''
    with open(nombre_archivo, 'r', encoding = 'utf-8') as archivo:
        info = json.load(archivo)
        jugadores = info[clave]
        return jugadores

def imprimir_dato(dato):
    '''
    # Esta función la utilizamos para imprimir un dato por consola.
    # Recibe por parametro el dato a imprimir.
    # No retorna, solo imprime.
    '''
    print(dato)

def imprimir_menu():
    '''
    # Esta función acumula los diversos items de selección, por los que el usuario interactuará.
    # Retorna el menú de lo antes mencionado.
    '''
    menu = '\n1) Mostrar la lista de todos los jugadores del Dream Team. '
    menu += '\n2) '
    menu += '\n3) '
    menu += '\n4) '
    menu += '\n5) '
    menu += '\n6) '
    menu += '\n7) '
    menu += '\n8) '
    menu += '\n9) '
    menu += '\n10) '
    menu += '\n11) '
    menu += '\n12) '
    menu += '\n13) '
    menu += '\n14) '
    menu += '\n15) '
    menu += '\n16) '
    menu += '\n17) '
    menu += '\n18) '
    menu += '\n19) '
    menu += '\n20) '
    menu += '\n21) '
    menu += '\n22) '
    menu += '\n23) '
    menu += '\n24) Salir.'
    return imprimir_dato(menu)