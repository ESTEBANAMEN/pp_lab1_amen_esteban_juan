import json
import csv
import re

def leer_json_dream_team(nombre_archivo: str, clave:str):
    '''
	\nEsta funcion lee el archivo .json del Dream team, mas especificamente sobre la info de los jugadores.
    \nRecibe por parametros la ruta del archivo .json y un string para acceder a los jugadores
    \nRetorna una lista de diccionarios con los datos de los jugadores.
    '''
    with open(nombre_archivo, 'r', encoding = 'utf-8') as archivo:
        info = json.load(archivo)
        jugadores = info[clave]
        return jugadores

def imprimir_dato(dato):
    '''
    \nEsta función la utilizamos para imprimir un dato por consola.
    \nRecibe por parametro el dato a imprimir.
    \nNo retorna, solo imprime.
    '''
    print(dato)

def imprimir_menu():
    '''
    \nEsta función acumula los diversos items de selección, por los que el usuario interactuará.
    \nRetorna el menú de lo antes mencionado.
    '''
    menu =  '\n1) Mostrar la lista de todos los jugadores del Dream Team. '
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

def validar_opcion_numerica(opcion:str) -> int:
    '''
    \nEsta función verifica que la opción ingresada sea un numero entre el 1 y el 24 inclusives.
    \nRecibe por parametro la opción tipo string.
    \nRetorna la opción en tipo int en caso de que sea valido el dato ingresado y en caso contrario, devuelve el valor 25(opción invalida en el menú).
    '''
    if re.search(r'^([1-9]{1,2}$)', opcion) and int(opcion) < 25:
        return int(opcion)
    else:
        return 25

def mostrar_jugadores_y_posicion(lista_jugadores: list[dict]):
    '''
    \nEsta función muestra el nombre y la posición de los jugadores de la lista.
    \nRecibe por parametro la lista de jugadores.
    \nNo retorna, imprime utilizando una función ya definida.
    '''
    print("")
    for jugador in lista_jugadores:
        nombre = jugador['nombre']
        posicion = jugador['posicion']
        if len(nombre) < 18:
            imprimir_dato(f"Nombre: {nombre}" + f"\t"*2 + f"Posición: {posicion}")
        else:
            imprimir_dato(f"Nombre: {nombre}\tPosición: {posicion}")