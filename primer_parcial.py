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
    menu += '\n4) Buscar un jugador por su nombre y mostrar sus logros.'
    menu += '\n5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. .'
    menu += '\n6) Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.'
    menu += '\n7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.'
    menu += '\n8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.'
    menu += '\n9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.'
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
                while True:
                    imprimir_menu()
                    opcion = validar_opcion_numerica(input("Para guardar elija la opcion 3: "))
                    if opcion == 3:
                        nombre_del_archivo = f"C:.\jugadores_csv\estadisticas_{reemplazar_espacios_por_guion_y_lower(jugador_seleccionado['nombre'])}.csv"
                        guardar_archivo(nombre_del_archivo, mensaje_estadisticas)
                        break
                    else:
                        imprimir_dato("\nLa 3, dije!")
            break
        else: 
            imprimir_dato("\nIndice Erroneo!! Intentalo nuevamente.")

#################################################### PUNTOS 4 y 6 ####################################################

def buscar_jugador_por_nombre_logros(lista_jugadores:list[dict], punto:int):
    '''
    \nEsta función permite que el usuario ingrese ciertos caracteres con los cuales se buscarán coincidencias en los nombres de los jugadores, para luego mediante estos, acceder a los logros.
    \nRecibe como parametro la lista de diccionarios que representan los jugadores y un entero que representa la opcion del menú elegida por el usuario.
    \nNo retorna, pero imprime el nombre y los logros (para el punto 4) o si dentro de ellos tiene la membresia en el salon de la fama (punto 6) segun el match que devuelve el re.search.
    '''
    nombre = input("\nIngrese el nombre del jugador: ").capitalize()
    imprimir_dato("")
    booleano = False
    for jugador in lista_jugadores:
        if re.search(nombre, jugador['nombre']):
            booleano = True
            if punto == 4:
                frase_con_nombre = f"Logros de: {jugador['nombre']}"
                imprimir_dato(frase_con_nombre)
                for logro in jugador['logros']:
                    imprimir_dato(logro)
                imprimir_dato("")
            elif punto == 6:
                for logro in jugador['logros']:
                    if logro == "Miembro del Salon de la Fama del Baloncesto":
                        imprimir_dato(f"{jugador['nombre']} es {logro}")
    if booleano:
        pass
    else:
        imprimir_dato("\nNo hay coincidencias!")

#################################################### PUNTO 5 ####################################################

def ordenar_segun_p_p(diccionario_jugador_p_p:dict):
    '''
    \nEsta función nos permite realizar un ordenamiento segun valores numéricos almacenados en una lista. Por otro lado de forma paralela, interactuara con otra segunda lista que contiene cadenas de texto.
    \nRecibe por parametro un diccionario con los nombres de los jugadores como claves y el promedio de puntos por partido como valores.
    \nNo retorna. Imprime, mediante una iteración las nombres y los pomedios en forma ordenada-ascendente.
    '''
    claves = list(diccionario_jugador_p_p.keys())
    valores = list(diccionario_jugador_p_p.values())
    cantidad_de_indices = len(valores)
    for indice in range(cantidad_de_indices):
        indice_minimo = indice
        for indice2 in range(indice + 1, cantidad_de_indices):
            if valores[indice2] < valores[indice_minimo]:
                indice_minimo = indice2
        valores[indice], valores[indice_minimo] = valores[indice_minimo], valores[indice]
        claves[indice], claves[indice_minimo] = claves[indice_minimo], claves[indice]
    imprimir_dato(f"Jugadores ordenados por puntos por partido y de forma ascendente:")
    for indice in range(cantidad_de_indices):
        clave = claves[indice]
        valor = valores[indice]
        imprimir_dato(f"{clave}: {valor}")

def acumular_promediar(lista_jugadores:list[dict]):
    '''
    \nEsta función acumula los promedios de puntos por partido de los jugadores, los promedia y almacena los nombres y valores mencionados en un diccionario.
    \nRecibe por parametro la lista de diccionarios correspondientes a los jugadores del Dream Team.
    \nNo retorna. Esta imprime los datos mencionados y trabaja en conjunto con otra función, permitiendo imprimir todo de forma ordenada.
    '''
    imprimir_dato("")
    acumulador_de_puntos_p_p = 0
    diccionario_jugador_p_p = {}
    for jugador in lista_jugadores:
        acumulador_de_puntos_p_p += jugador['estadisticas']['promedio_puntos_por_partido']
        if jugador['nombre'] not in diccionario_jugador_p_p:
            diccionario_jugador_p_p[jugador['nombre']] = jugador['estadisticas']['promedio_puntos_por_partido']
    imprimir_dato(f"El total del promedio de puntos por partido es: {acumulador_de_puntos_p_p}\n")
    imprimir_dato(f"El promedio del total mencionado es: {acumulador_de_puntos_p_p/len(lista_jugadores)}\n")
    ordenar_segun_p_p(diccionario_jugador_p_p)

#################################################### PUNTOS 7, 8 y 9 ####################################################

def iterar_jugadores_calcular_max_y_mostrar(lista_jugadores:list[dict],estadistica_a_evaluar:str):
    '''
    \nEsta función no busca un valor maximo entre ciertas estadisticas solicitadas y hardcodeadas desde el main.py.
    \nRecibe por parametros la lista de diccionarios (jugadores) y una cadena de texto correspondiente a la estadistica, cuyo valor sera evaluado entre todos los jugadores.
    \nNo retorna. Imprime un mensaje adaptado, informando el nombre y la cantidad que representa el maximo de los valores correspondientes a la estadistica hardcodeada.
    '''
    nombre_estadistica_max = ""
    estadistica_max = 0
    for jugador in lista_jugadores:
        if jugador['estadisticas'][estadistica_a_evaluar] > estadistica_max:
            nombre_estadistica_max = jugador['nombre']
            estadistica_max = jugador['estadisticas'][estadistica_a_evaluar]
    estadistica_final = estadistica_a_evaluar.replace("_", " ")
    if re.search(r"^porcentaje tiros",estadistica_final):
        estadistica_final = re.sub(r"porcentaje tiros", "porcentaje de tiros", estadistica_final)
    mensaje = f"El jugador con mas {estadistica_final} es {nombre_estadistica_max}, con la cantidad de {estadistica_max}"
    imprimir_dato("")
    imprimir_dato(mensaje)