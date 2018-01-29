import random
print("Piedra, papel, tijeras, lagarto, spock!")
salir = False
while not salir:
    mi_jugada = input("Elige: ")
    maquina = random.randint(1,5)
    if maquina == 1:
        su_jugada = "piedra"
    elif maquina == 2:
        su_jugada = "papel"
    elif maquina == 3:
        su_jugada = "tijeras"
    elif maquina == 4:
        su_jugada = "lagarto"
    else:
        su_jugada = "spock"
    print(mi_jugada," contra ",su_jugada)
    if mi_jugada == su_jugada:
        print("Empate!")
    elif mi_jugada == "piedra":
        if su_jugada == "papel" or su_jugada == "spock":
            print("Has perdido")
        else:
            print("Has ganado")
    elif mi_jugada == "papel":
        if su_jugada == "lagarto" or su_jugada == "tijeras":
            print("Has perdido")
        else:
            print("Has ganado")
    elif mi_jugada == "tijeras":
        if su_jugada == "spock" or su_jugada == "piedra":
            print("Has perdido")
        else:
            print("Has ganado")
    elif mi_jugada == "lagarto":
        if su_jugada == "piedra" or su_jugada == "tijeras":
            print("Has perdido")
        else:
            print("Has ganado")
    else:
        if su_jugada == "papel" or su_jugada == "lagarto":
            print("Has perdido")
        else:
            print("Has ganado")
    repetir_pregunta = True
    while repetir_pregunta:
        seguir = input("¿Echamos otra? (s/n)")
        if seguir == "s":
            repetir_pregunta = False
        elif seguir =="n":
            repetir_pregunta = False
            salir = True
        else:
            print("No entiendo :(")
            repetir_pregunta = True
        
                        