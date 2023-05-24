import json
import csv
import re


def leer_json_dream_team(nombre_archivo: str, clave: str):
    '''
    \nEsta funcion lee el archivo .json del Dream team, mas especificamente sobre la info de los jugadores.
    \nRecibe por parametros la ruta del archivo .json y un string para acceder a los jugadores
    \nRetorna una lista de diccionarios con los datos de los jugadores.
    '''
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        info = json.load(archivo)
        jugadores = info[clave]
        return jugadores

#################################################### FUNCIONES UTILES ####################################################
def imprimir_dato(dato):
    '''
    \nEsta función la utilizamos para imprimir un dato por consola.
    \nRecibe por parametro el dato a imprimir.
    \nNo retorna, solo imprime.
    '''
    print(dato)

def validar_opcion_numerica(opcion: str) -> int:
    '''
    \nEsta función verifica que la opción ingresada sea un numero entre el 1 y el 24 inclusives.
    \nRecibe por parametro la opción tipo string.
    \nRetorna la opción en tipo int en caso de que sea valido el dato ingresado y en caso contrario, devuelve el valor 25 (en el menú: "opción invalida").
    '''
    if re.search(r'^([1-9]{1,2}$)', opcion) and int(opcion) < 25:
        return int(opcion)
    else:
        return 25

def reemplazar_guion_por_espacio_y_capitalizar(cadena:str) -> str:
    '''
    \nEsta función nos permite separar por "espacios" en lugar del "guion bajo" dado en las cadenas de texto y coloca en mayúscula la primer letra.
    \nRecibe por parametro una cadena de texto, la cual se espera esté separada mediante el uso de "guion bajo".
    \nRetorna a la cadena recibida con los guiones, reemplazados por espacios y capitalizada (primer letra en mayúscula).
    '''
    cadena_modificada = cadena.replace("_", " ")
    cadena_modificada = cadena_modificada.capitalize()
    return cadena_modificada

def reemplazar_espacios_por_guion_y_lower(cadena:str) -> str:
    '''
    \nEsta función nos permite separar por "guion bajo" en lugar del "espacio" dado en las cadenas de texto y transformar en minúsculas las letras.
    \nRecibe por parametro una cadena de texto, la cual se espera esté separada mediante el uso de "espacios".
    \nRetorna a la cadena recibida con los espacios, reemplazados por guion bajo y lowerizada (todas las letras en minúscula).
    '''
    cadena_modificada = cadena.replace(" ", "_")
    cadena_modificada = cadena_modificada.lower()
    return cadena_modificada

def guardar_archivo(nombre_archivo:str, contenido_a_guardar:str) -> bool:
    '''
    \nEsta función nos permite guardar determinados datos en un archivo.
    \nRecibe por parametros el nombre del archivo (ruta)  y el contenido a volcar en dicho archivo.
    \nNo retorna, pero imprime un mensaje para los casos en que se cree o no el archivo.
    '''
    booleano = False
    with open(nombre_archivo, "w+", encoding = 'utf-8') as archivo:
        archivo.writelines(contenido_a_guardar)
        booleano = True
        mensaje = f"\nSe creó el archivo exitosamente: {nombre_archivo}"
    if booleano:
        print(mensaje)
    else:
        mensaje = f"\nERROR al crear el archivo: {nombre_archivo}"
        print(mensaje)

##########################################################################################################################

def imprimir_menu():
    '''
    \nEsta función acumula los diversos items de selección, por los que el usuario interactuará.
    \nRetorna el menú de lo antes mencionado.
    '''
    menu = '\n1) Mostrar la lista de todos los jugadores del Dream Team.'
    menu += '\n2) Seleccionar un jugador por su indice y mostrar sus estadisticas.'
    menu += '\n3) Guardar en un archivo, de extensión .csv, los datos del punto anterior.'
    menu += '\n4) .'
    menu += '\n5) .'
    menu += '\n6) .'
    menu += '\n7) .'
    menu += '\n8) .'
    menu += '\n9) .'
    menu += '\n10) .'
    menu += '\n11) .'
    menu += '\n12) .'
    menu += '\n13) .'
    menu += '\n14) .'
    menu += '\n15) .'
    menu += '\n16) .'
    menu += '\n17) .'
    menu += '\n18) .'
    menu += '\n19) .'
    menu += '\n20) .'
    menu += '\n21) .'
    menu += '\n22) .'
    menu += '\n23) .'
    menu += '\n24) Salir.'
    return imprimir_dato(menu)

#################################################### PUNTO 1 ####################################################
def mostrar_jugadores_y_posicion(lista_jugadores:list[dict]):
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
            imprimir_dato(f"Nombre: {nombre}" + f"\t" *2 + f"Posición: {posicion}")
        else:
            imprimir_dato(f"Nombre: {nombre}\tPosición: {posicion}")

#################################################### PUNTOS 2 y 3 ####################################################

def mostrar_estadisticas_jugador(jugador: dict):    
    '''
    \nEsta función itera sobre un diccionario para almacenar ciertas claves y valores para luego ser impresos.
    \nRecibe por parametro un diccionario que representa a un jugador, captado desde otra función.
    \nRetorna la informacion que luego será utilizada para generar un archivo .csv en otra función, y también imprime por consola un mensaje con las claves y valores respectivas a las estadisticas de un jugador.
    '''
    mensaje = ""
    mensaje_para_csv = f"{jugador['nombre']}\nPosicion: {jugador['posicion']}\n"
    for clave, valor in jugador['estadisticas'].items():
        estadisticas = reemplazar_guion_por_espacio_y_capitalizar(clave)
        mensaje += f"{estadisticas}: {valor}\n"
    mensaje_para_csv += mensaje
    imprimir_dato(mensaje)
    return mensaje_para_csv

def indices_con_nombres(lista_jugadores:list[dict]):
    '''
    \nEsta función itera sobre la lista de jugadores, generando un indice por el cual se obtendra el diccionario correspondiente al jugador en esa posicion.
    \nRecibe por parametro la lista de jugadores.
    \nNo retorna. Pero imprime, en prinicipio, un menú de seleccion en base al indice generado. Y por medio de otra función las estadisticas seleccionadas. Así mismo, si el usuario asi lo desea, se activa la opcion del ejercicio número 3, la cual permite crear y almacenar en un archivo .csv la informacion mostrada.
    '''
    indice = 0
    imprimir_dato("")
    for jugador in lista_jugadores:
        imprimir_dato(f"{indice}- {jugador['nombre']}")
        indice += 1
    while True:
        opcion = input("\nSeleccione el índice de un jugador: ")
        indice = int(opcion)
        if indice >= 0 and indice < len(lista_jugadores):
            jugador_seleccionado = lista_jugadores[indice]
            imprimir_dato(f"\nEstadísticas de {jugador_seleccionado['nombre']}:")
            mensaje_estadisticas = mostrar_estadisticas_jugador(jugador_seleccionado)
            guardar = input("\n3) Desea guardar los datos del jugador mostrado? \nSi = s\nNo = tecla cuakquiera\n")
            if guardar == 's' or guardar == 'S':
                nombre_del_archivo = f"C:.\jugadores_csv\estadisticas_{reemplazar_espacios_por_guion_y_lower(jugador_seleccionado['nombre'])}.csv"
                guardar_archivo(nombre_del_archivo, mensaje_estadisticas)
            break
        else: 
            imprimir_dato("\nIndice Erroneo!! Intentalo nuevamente.")

#################################################### PUNTO 4 ####################################################

def buscar_jugador_por_nombre(lista_jugadores:list[dict]):
    '''
    \nEsta función permite que el usuario ingrese ciertos caracteres con los cuales se buscarán coincidencias en los nombres de los jugadores, para luego mediante estos, acceder a los logros.
    \nRecibe como parametro la lista de diccionarios que representan los jugadores.
    \nNo retorna, pero imprime el nombre y los logros, segun el match que devuelve el re.search.
    '''
    nombre = input("\nIngrese el nombre del jugador: ").capitalize()
    imprimir_dato("")
    booleano = False
    for jugador in lista_jugadores:
        if re.search(nombre, jugador['nombre']):
            frase_con_nombre = f"Logros de: {jugador['nombre']}"
            imprimir_dato(frase_con_nombre)
            booleano = True
            for logro in jugador['logros']:
                imprimir_dato(logro)
            imprimir_dato("")
    if booleano:
        pass
    else:
        imprimir_dato("\nNo hay coincidencias!")
