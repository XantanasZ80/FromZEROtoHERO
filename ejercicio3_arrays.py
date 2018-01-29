import random
def PiedraPapel():
    opciones = ["piedra","papel","tijeras","lagarto","spock"]
    print("Piedra, papel, tijeras, lagarto, spock!")
    salir = False
    while not salir:
        jugador = input("Elige: ")
        mi_jugada = jugador.lower() #paso la entrada a minusculas
        maquina = random.randint(0,4)
        su_jugada = opciones[maquina]
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
        elif mi_jugada == "spock":
            if su_jugada == "papel" or su_jugada == "lagarto":
                print("Has perdido")
            else:
                print("Has ganado")
        else:
            print("No entiendo")
        repetir_pregunta = True
        while repetir_pregunta:
            seguir = input("¿Echamos otra? (s/n)")
            if seguir.lower() == "s":
                repetir_pregunta = False
            elif seguir.lower() =="n":
                repetir_pregunta = False
                salir = True
            else:
                print("No entiendo :(")
                repetir_pregunta = True
    return
def Adivina(intentos):
    print("Adivina el numero del 1 al 100:")
    numero = random.randint(1,100)
    #print(numero)
    while intentos > 0:
        print("Quedan",intentos,"intentos")
        opcion = int(input("Numero? "))
        if opcion == numero:
            print("Acertaste!!")
            intentos = 0
        elif opcion < numero:
            print("Es mayor")
            intentos = intentos -1
            if intentos == 0:
                print("Perdiste, era el ",numero)
        else:
            print("Es menor")
            intentos = intentos -1
            if intentos == 0:
                print("Perdiste, era el",numero)
    return
salir = False
while not salir:
    print("¿A que jugamos?")
    print("A - Piedra, papel, tijeras, lagarto, Spock")
    print("B - Adivina el numero")
    print("X - Salir")
    juego = input("Elige, A o B ").upper() #Lo convierto a mayusculas
    if juego == "A":
        PiedraPapel()
    elif juego =="B":
        intentos = int(input("Numero de intentos:"))
        Adivina(intentos) 
    elif juego == "X":
        salir = True
    else:
        print("No te entiendo :(")
                     
        
                        