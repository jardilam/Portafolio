# Variable para el puntaje total (Los puntajes de cada ronda entrarán acá):
punjTot = []

# Función para mostrar el puntaje:
# Ronda 1:
def puntaje1(resCorrectas, res):
    print("Dinero obtenido: ")
    punj1 = resCorrectas
    if punj1 > 10:
        print("$", punj1)
        print("Pasas a la siguiente ronda")
    elif punj1 < 9:
        print("$", punj1)
        print("Perdiste")
    punjTot.append(punj1)
# Ronda 2:
def puntaje2(resCorrectas, res):
    print("Dinero obtenido: ")
    punj2 = resCorrectas
    if punj2 > 20:
        print("$", punj2)
        print("Pasas a la siguiente ronda")
    elif punj2 < 19:
        print("$", punj2)
        print("Perdiste")
    punjTot.append(punj2)
# Ronda 3:
def puntaje3(resCorrectas, res):
    print("Dinero obtenido: ")
    punj3 = resCorrectas
    if punj3 > 30:
        print("$", punj3)
        print("Pasas a la siguiente ronda")
    elif punj3 < 29:
        print("$", punj3)
        print("Perdiste")
    punjTot.append(punj3)
# Ronda 4:
def puntaje4(resCorrectas, res):
    print("Dinero obtenido: ")
    punj4 = resCorrectas
    if punj4 > 40:
        print("$", punj4)
        print("Pasas a la siguiente ronda")
    elif punj4 < 39:
        print("$", punj4)
        print("Perdiste")
    punjTot.append(punj4)
# Ronda 5:
def puntaje5(resCorrectas, res):
    print("Dinero obtenido: ")
    punj5 = resCorrectas
    if punj5 > 250:
        print("$", punj5)
        print("Pasas a la siguiente ronda")
    elif punj5 < 249:
        print("$", punj5)
        print("Perdiste")
    punjTot.append(punj5)
# Puntaje total durante la partida:
def puntajeTot():
    total = sum(punjTot)
    if total < 359:
        print("Obtuviste: ", "$", total)
        print("Desafortunadamente no alcanzaste el objetivo. Más suerte a la próxima")
    else:
        print("Obtuviste: ", "$", total)
        print("¡Excelente!")
        print("""
               .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
