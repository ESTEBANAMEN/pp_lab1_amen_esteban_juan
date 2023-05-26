from primer_parcial import (leer_json_dream_team,
							imprimir_dato,
                            imprimir_menu,
							validar_opcion_numerica,
							mostrar_jugadores_y_posicion,
							indices_con_nombres,
							buscar_jugador_por_nombre,
							mostrar_logros_jugador,
							acumular_promediar,
							iterar_jugadores_calcular_max_y_mostrar,
							mostrar_jugadores_que_superan_el_valor
							)

def dream_team_app():
	'''
	\nEsta función es utilizada para interactuar con el menu de opciones, siendo asi la función principal.
	'''
	equipo_dream_team = leer_json_dream_team('dt.json', 'jugadores')
	while True:
		imprimir_menu()
		opcion = validar_opcion_numerica(input("Opcion a elegir: "))

		match(opcion):
			case 1:
				mostrar_jugadores_y_posicion(equipo_dream_team)
			case 2:
				indices_con_nombres(equipo_dream_team)
			case 3:
				print('\nEste punto se utiliza junto con el anterior. Usted debe visualizar primeramente si lo que va a guardar es de su agrado!')
			case 4:
				nombre = input("\nIngrese el nombre del jugador del cual quiere visualizar los correspondientes logros: ").capitalize()
				imprimir_dato("")
				while not buscar_jugador_por_nombre(nombre, equipo_dream_team):
					nombre = input("\nNo hay coincidencias! Ingrese el nombre del jugador del cual quiere visualizar los correspondientes logros: ").capitalize()
					imprimir_dato("")
				mostrar_logros_jugador(nombre, equipo_dream_team, opcion)
			case 5:
				acumular_promediar(equipo_dream_team)
			case 6:
				nombre = input("\nIngrese el nombre del jugador del cual quiere visualizar los correspondientes logros: ").capitalize()
				imprimir_dato("")
				while not buscar_jugador_por_nombre(nombre, equipo_dream_team):
					nombre = input("\nNo hay coincidencias! Ingrese el nombre del jugador del cual quiere visualizar los correspondientes logros: ").capitalize()
					imprimir_dato("")
				mostrar_logros_jugador(nombre, equipo_dream_team, opcion)
			case 7:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'rebotes_totales')
			case 8:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'porcentaje_tiros_de_campo')
			case 9:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'asistencias_totales')
			case 10:
				mostrar_jugadores_que_superan_el_valor(equipo_dream_team, 'promedio_puntos_por_partido')
			case 11:
				mostrar_jugadores_que_superan_el_valor(equipo_dream_team, 'promedio_rebotes_por_partido')
			case 12:
				mostrar_jugadores_que_superan_el_valor(equipo_dream_team, 'promedio_asistencias_por_partido')
			case 13:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'robos_totales')
			case 14:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'bloqueos_totales')
			case 15:
				pass
			case 16:
				pass
			case 17:
				pass
			case 18:
				pass
			case 19:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'temporadas')
			case 20:
				pass
			case 21:
				pass
			case 22:
				pass
			case 23:
				pass
			case 24:
				print("CERRANDO PROGRAMA! UN SALUDO.")
				break
			case 25:
				print("\nOpción invalida!!")
dream_team_app()