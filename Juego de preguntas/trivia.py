from preguntas import *
from rondas import *


# Comienzo del juego:
print ("Bienvenido/a")
print("Hoy vamos a jugar una trivia en donde se aumentará el nivel de dificultad a medida que avanzas.")
print("A medida que respondas correctamente irás ganando $10 por cada pregunta")
print ("¿Quieres jugar?")
print ("Si")
print ("No")
opcion = input("> ")

if opcion == "Si":
    print("¡Vamos a jugar!")
    print("""
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  |.'\    |===| |--|%%|   |  |
|%%|   |  |\.'\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \.'\ |   |_|__|  |~~~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--' 
""")
    print("---------------------")
    print("Ronda 1")
    print("---------------------")
    ronda1()
    print("---------------------")
    print("Ronda 2")
    print("---------------------")
    ronda2()
    print("---------------------")
    print("Ronda 3")
    print("---------------------")
    ronda3()
    print("---------------------")
    print("Ronda 4")
    print("---------------------")
    ronda4()
    print("---------------------")
    print("Ronda 5")
    print("En esta ronda ganarás $50 por cada pregunta que respondas correctamente")
    print("---------------------")
    ronda5()
    print("---------------------")
    print("Puntaje total: ")
    puntajeTot()
else:
    print("Hasta pronto")