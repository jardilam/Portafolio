from preguntas import *
from puntaje import *
from revision import *

# Ronda 1:

def ronda1():
    respuestasAcum = []
    resCorrectas = 0
    numeroPregunta = 1
    for p in preguntasFac1:
        print(p)
        for r in respuestasFac1[numeroPregunta - 1]:
            print(r)
        res = input("Ingresa solo una opción: ")
        res = res.upper()
        respuestasAcum.append(res)
        resCorrectas += revision(preguntasFac1.get(p), res)
        numeroPregunta += 1
    
    puntaje1(resCorrectas, res)

# Ronda 2:

def ronda2():
    respuestasAcum = []
    resCorrectas = 0
    numeroPregunta = 1
    for p in preguntasFac2:
        print(p)
        for r in respuestasFac2[numeroPregunta - 1]:
            print(r)
        res = input("Ingresa sólo una opción: ")
        res = res.upper()
        respuestasAcum.append(res)
        resCorrectas += revision(preguntasFac2.get(p), res)
        numeroPregunta += 1
    
    puntaje2(resCorrectas, res)

#Ronda 3:

def ronda3():
    respuestasAcum = []
    resCorrectas = 0
    numeroPregunta = 1
    for p in preguntasMed1:
        print(p)
        for r in respuestasMed1[numeroPregunta - 1]:
            print(r)
        res = input("Ingresa sólo una opción: ")
        res = res.upper()
        respuestasAcum.append(res)
        resCorrectas += revision(preguntasMed1.get(p), res)
        numeroPregunta += 1
    
    puntaje3(resCorrectas, res)

#Ronda 4:

def ronda4():
    respuestasAcum = []
    resCorrectas = 0
    numeroPregunta = 1
    for p in preguntasMed2:
        print(p)
        for r in respuestasMed2[numeroPregunta - 1]:
            print(r)
        res = input("Ingresa sólo una opción: ")
        res = res.upper()
        respuestasAcum.append(res)
        resCorrectas += revision(preguntasMed2.get(p), res)
        numeroPregunta += 1
    
    puntaje4(resCorrectas, res)

#Ronda 5:

def ronda5():
    respuestasAcum = []
    resCorrectas = 0
    numeroPregunta = 1
    for p in preguntasDif1:
        print(p)
        for r in respuestasDif1[numeroPregunta - 1]:
            print(r)
        res = input("Ingresa sólo una opción: ")
        res = res.upper()
        respuestasAcum.append(res)
        resCorrectas += revRonda5(preguntasDif1.get(p), res)
        numeroPregunta += 1
    
    puntaje5(resCorrectas, res)