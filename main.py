from primer_parcial import (leer_json_dream_team,
                            imprimir_menu,
							validar_opcion_numerica,
							mostrar_jugadores_y_posicion,
							indices_con_nombres,
							buscar_jugador_por_nombre_logros,
							acumular_promediar,
							iterar_jugadores_calcular_max_y_mostrar
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
				buscar_jugador_por_nombre_logros(equipo_dream_team, opcion)
			case 5:
				acumular_promediar(equipo_dream_team)
			case 6:
				buscar_jugador_por_nombre_logros(equipo_dream_team, opcion)
			case 7:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'rebotes_totales')
			case 8:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'porcentaje_tiros_de_campo')
			case 9:
				iterar_jugadores_calcular_max_y_mostrar(equipo_dream_team,'asistencias_totales')
			case 10:
				pass
			case 11:
				pass
			case 12:
				pass
			case 13:
				pass
			case 14:
				pass
			case 15:
				pass
			case 16:
				pass
			case 17:
				pass
			case 18:
				pass
			case 19:
				pass
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