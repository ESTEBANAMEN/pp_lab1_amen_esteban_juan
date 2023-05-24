from primer_parcial import (leer_json_dream_team,
                            imprimir_menu,
							validar_opcion_numerica,
							mostrar_jugadores_y_posicion,
							indices_con_nombres
							)

def dream_team_app():
	'''
	\nEsta función es utilizada para interactuar con el menu de opciones, siendo asi la función principal.
	'''
	equipo_dream_team = leer_json_dream_team('dt.json', 'jugadores')
	while True:
		imprimir_menu()
		opcion = validar_opcion_numerica(input("Opcion a elejir: "))

		match(opcion):
			case 1:
				mostrar_jugadores_y_posicion(equipo_dream_team)
			case 2:
				indices_con_nombres(equipo_dream_team)
			case 3:
				pass
			case 4:
				pass
			case 5:
				pass
			case 6:
				pass
			case 7:
				pass
			case 8:
				pass
			case 9:
				pass
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