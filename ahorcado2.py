# Juego que simula el ahorcado.
# Puedes cometer 6 fallos
# Importaciones
# ----------------------------------------------------------
import random
from os import system, name

# Constantes
# ----------------------------------------------------------
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Funciones
# ----------------------------------------------------------
def clear(): 
  
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def elijeLetra(letrasUtilizadas): 
    # Devuelve la letra que el jugador introdujo. Esta función hace que el jugador introduzca una letra y no cualquier otra cosa 
    while True: 
        print ('Adivina una letra:') 
        letra = input() 
        letra = letra.lower() 
        if len(letra) != 1: 
            print ('Introduce una sola letra.') 
        elif letra in letrasUtilizadas: 
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?') 
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz': 
            print ('Elije una letra y no otro símbolo.') 
        else: 
            return letra 

# Variables
# ----------------------------------------------------------
palabras_disponibles = ["azul", "flor","casa","comer","desoxirribonucleico"]

# Programa Principal
# ----------------------------------------------------------
#elgir la palabra a adivinar
palabra_secreta = palabras_disponibles[random.randint(0,len(palabras_disponibles))]
guiones = "_" * len(palabra_secreta)
letras_usadas = []

#iniciar el juego
juego = True
cadalso = 0
while juego == True:
    if "_" in guiones and cadalso < 6:
        #pedir la letra
        print(AHORCADO[cadalso])
        print("palabra:",guiones)
        print("letras falladas",letras_usadas)
        letra_pedida = elijeLetra("".join(letras_usadas) + guiones)
        clear()
        #decir si esta en la palabra
        indice = 0
        for i in palabra_secreta:
            if letra_pedida == i:
                guiones = guiones[:indice] + letra_pedida + guiones[indice+1:] 
            indice = indice + 1
        #si no esta en la palabra, lo indica y dibuja una parte
        if letra_pedida not in palabra_secreta:
            print("prueba otra vez")
            letras_usadas.append(letra_pedida)
            cadalso = cadalso + 1
        #muestra la interfaz
        print(AHORCADO[cadalso])
        print("palabra:",guiones)
        print("letras falladas",letras_usadas)
    #Cuando aciertas todas las letras
    elif "_" not in guiones:
        juego = False
        clear()
        print(AHORCADO[cadalso])
        print("palabra:",guiones)
        print("letras falladas",letras_usadas)
        print("HAS GANADO!!!")
    #Cuando se dibuja el ahorcado
    elif cadalso >= 6:
        clear()
        juego = False
        print(AHORCADO[cadalso])
        print("palabra:",guiones)
        print("letras falladas",letras_usadas)
        print("HAS PERDIDO!!! La palabra era",palabra_secreta)