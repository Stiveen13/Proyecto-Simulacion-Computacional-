"""

Clase Simulcaion:
Clase encargada de la simución del problema

Alvaro Javier Quintero Peña - 201556009
Kevin Santiago Lemos López - 201556168
Stiveen Correa Escobar - 201556213

"""

#Importancion de las librerias necesarias para esta solucion al problema del Maestro del ajedrez con N reinas
#En profundización de los robots contra los humanos

from pygame.locals import *
from random import sample
from collections import *
from time import time
import pygame,sys
import random
import numpy

#INICIO DEL TOUR. DIVIÉRTETE

#=======================================================================================================================

#****************************************** Solución problema tipo LAS VEGAS *******************************************

#FUNCIONES CHALLENGER EN LEAGUE OF LEGENDS, dan solucion al problema por eso son expertas en lol

#valida que en las posiciones anteriores a la ingresada no haya un valor menor en diagonal
#valida por el valor actual de la posicion ingresada
#Cabe resaltar que tiene este nombre en honor a su función y lógica
#dia = diagonal, 45 = menores al valor de la posicion, dia = lógíca de la diapositiva del profe
def diag45dia(vec, pos):
    #print("soy la funcion diag45")
    aux = True
    val = vec[pos]
    #print("valor = ", val, "pos = ", pos)
    k = 1
    #print("tamaño vec = ", len(vec))
    #if pos < 1:
     #   return True
    for i in range(pos, -1, -1):
        #val = vec[i]
        #print("pos ante = ", i - 1)
        #print("val ante = ", val - k)
        #print(i)
        #print(k)
        #if i - 1 < 0:
         #   print("salí porque llegué a pos -1")
          #  return aux
        if vec[i - 1] == val - k:
            #print("No estoy libre")
            #return True
            aux = False
            #return print(aux)
            return aux
        else:
            #print("estoy libre")
            #return True
            aux = True
        k = k + 1
    #print("termine funcion diag45")
    return aux
    #return print(aux)

#lista = [1, 3, 0, 2]
#print(lista[-3])
#print(diag45dia(lista,2))

#valida que en las posiciones anteriores a la ingresada no haya un valor mayor en diagonal
#valida por el valor actual de la posicion ingresada
#Cabe resaltar que tiene este nombre en honor a su función y lógica
#dia = diagonal, 135 = mayores al valor de la posicion, dia = lógíca de la diapositiva del profe
def diag135dia(vec, pos):
    #print("soy la funcion diag135")
    aux = True
    val = vec[pos]
    #print("valor= ", val, "pos = ", pos)
    k = 1
    if pos < 1:
        return True
    for i in range(pos, -1, -1):
        #if i == 0: i = i + 1
        #val = vec[i]
        #print("pos ante = ", pos - 1)
        #print("val ante = ", val + 1)
        #print(i)
        #print(k)
        if vec[i - 1] == val + k:
            #print("No estoy libre")
            aux = False
            #return print(aux)
            return  False
        else:
            #print("estoy libre")
            #return
            aux = True
        k = k + 1
    #print("termine funcion diag135")
    return aux
    #return print(aux)

#lista = [0, 5, 3, 1, 4, 0, 6, 7]
#print(diag135dia(lista,0))
#diag45dia(lista,4)

#Esta hermosa es la encargadade genera de un vector de números aleatorios de tamaño cantidad y números entre min y max
#Pero es PRO porque cada vez que se ejecuta genera aleatorios diferentes

#global alea

def aleatoriosNumpy(cantidad, min, max):
    numeros = []
    alea = []
    c = 0
    while len(alea) < cantidad:
        #print(len(numeros))
        #print(cantidad)
        #print(cantidad)
        #c = c + 1
        numero =  numpy.random.randint(max)
        #print(numero)
        if not numero in alea:
            alea.append(numero)
        #print(c)
        #print(numeros)
    #return print (numeros)
    return alea

#for i in range(10):
#    print(aleatoriosNumpy(4,1,4))

#aleatoriosNumpy(8,1,8)

#Esta mellisza junto con su hermana crearLista12 son las escargadas de llenar los arregos con 0 o -10 para posteriormente
#pintar el tablero, esta empieza con 0 para que el primer cuadro de cada fila sea blanco
def crearLista1(N):
    L = []
    for i in range(N):
        if i == 0:
            L.append(0)
        elif i%2 == 0:
            L.append(0)
        else :
            L.append(-10)
    return L

#Esta mellisza junto con su hermana crearLista1 son las escargadas de llenar los arregos con 0 o -10 para posteriormente
#pintar el tablero, esta empieza con -10 para que el primer cuadro de cada fila sea amarrillo
def crearLista12(N):
    L = []
    for i in range(N):
        if i == 0:
            L.append(-10)
        elif i%2 == 0:
            L.append(-10)
        else :
            L.append(0)
    return L

#funcion que crea un matriz de 0 y -10 para distinguir los colores y pone las reinas con valor 1000
def CreaMatriz(reinas):
    N = len(reinas)
    Matriz = []
    for i in range(N):
        if i == 0:
            Matriz.append(crearLista1(N))
        elif i%2 == 0:
            Matriz.append(crearLista1(N))
        else:
            Matriz.append(crearLista12(N))
    for i in range(N):
        Matriz[i][reinas[i]] = 1000
    return Matriz

#reinas = [1, 3, 0, 2]
#vecMat(reinas)
#CreaMatriz(reinas)

def unaleatorio(vec, n):
    aux = False
    while not aux:
        elem = numpy.random.randint(n)
        #print("soy elem", elem)
        if not elem in vec:
            aux = True
    return elem

#función que intenta resolver el problema, si lo temrmina (n reinas) retorna true
#si no terimina retorna la reina en la que falló y retorna false
def puedo(reinas, n):
    #d = aleatoriosNumpy(n, 1, n) #se crean posiciones aleatorias para las reinas
    #CreaMatriz(d)
    print("--------------------------------------------------------------------------------------------------------")
    for i in range (n):
        #disponibles = [0, 1, 2, 3, 4, 5, 6, 7]
        #elem = d[numpy.random.randint(n)] # se intenta hacer las reinas aleatorias, pero pone soluciones erroneas
        elem = unaleatorio(reinas, n) # se accede a una reina aleatoria de las disponibles
        reinas[i] = elem # ponemos nuestro elemto como reina para su evaluación
        #elem = numpy.random.randint(n)
        #print(i)
        #print("funcion mia 45: ", diag45dia(reinas,i))
        #print("Python     :", bool(diag45dia(d,i)))
        #print("funcion mia 135", diag135dia(reinas,i))
        #print("Python     :", bool(diag135dia(d, i)))
        aux = diag45dia(reinas,i) and diag135dia(reinas, i)
        #print("aux", aux)
        #if bool(diag45dia(reinas, i)) and bool(diag135dia(reinas, i)):
        if aux: # si cumple las condiciones se pone una reina
            reinas[i] = elem
        else: #return print('no puedo seguir, paré en la reina', i)
            #CreaMatriz(reinas)
            print('no puedo seguir, paré en la reina', i)
            return False
    print(reinas)
    #CreaMatriz(reinas)
    return True

#puedo([10, 10, 10, 10], 4)

#iniciaciliza un vector detamaño n (número de reinas) en 100
def llenarReinas(n):
    numeros = []
    while len(numeros) < n:
        numero =  100
        numeros.append(numero)
    return numeros

#reinas = [100, 100, 100, 100, 100, 100, 100, 100]
#puedo(reinas, 8)
#print(reinas)

#print(aleatorios(8,1,8))
#aleatorios(15,1,15)

#Funcion que da solicion al problema
#Llama a puedo si retorna true pues pinta solucion, en caso que retorne false vuelva a intentar
#hasta que soluciona el problema
#se le ingresa el tañano del tablero a llenar
def hastaQueTermine(n):
    tiempoInicial = time()
    fin = False
    while not fin:
        reinas = llenarReinas(n)
        #puedo(reinas,n)
        #print(reinas)
        fin = puedo(reinas, n)
    tiempoFinal = time()
    tiempoEjecucuion = tiempoFinal - tiempoInicial
    print("Tiempo de ejecucion las vegas con ", n,  " reinas: ", tiempoEjecucuion)
    return CreaMatriz(reinas)

#hastaQueTermine(4)

#**************************************************** FIN LAS VEGAS ***************************************************#
#
# #definimos nuestras piesas
# #cuadros del tablero
# gris = (183, 133, 77 )
# amarillo = (240, 144, 36 )
# Gris=pygame.image.load("gris.png")
# Amarillo=pygame.image.load("amarillo.png")
#
# #se pide el tamaño del tablero a solucionar
# n= int(input("ingrese el numero de reinas"))
#
# #cargamos la imagen de png fe la reina
# reina=pygame.image.load("reina.png")
#
# #se define el arreglo con el que pintará el tablero
# prueba=hastaQueTermine(n)
# print("SOY PRUEBAAAAAAAAAAAAAAAAAAAAAAAAAAAA", prueba)
# #prueba=[[0,2,0,-1],[-1,0,-1,0],[2,-1,0,-1],[-1,0,-1,2]]
#
# #Clase ventana para mostar la interfaz
# class ventana:
#     def tablero (matrix):
#        i=0
#        print(len (matrix))
#        for l in range(len(matrix)):
#            print("soy l",i)
#            j=0
#            for k in range(len(matrix)):
#             if(matrix[l][k]==-10): #si es -10 se pinta amarillo
#                 marco.blit(Amarillo,(i,j))
#                #pygame.draw.rect(marco, amarillo, [j, i, 36, 36], 0)
#                 j+=36
#                 #print("amarillo")
#             elif(matrix[l][k]==0): #si es 0 se pinta balco
#                 marco.blit(Gris,(i,j))
#                  #pygame.draw.rect(marco, gris, [j, i, 36, 36], 0)
#                     #print("girs")
#                 j+=36
#             else:
#                 marco.blit(reina,(i,j)) #en otro caso se pone la reina
#                     #print("reina")
#                 j+=36
#            i+=36
#        return 0
#
# #inicializacion de Pygame para el tablero
# pygame.init()
#
# # Establecemos el alto y largo de la pantalla
# #dimensiones = [700, 500]
# #marco= pygame.display.set_mode(dimensiones)
# marco= pygame.display.set_mode(((n*36),(n*36)))
# hecho=False
# #ancho = int(dimensiones[0] / n)
# #alto = int(dimensiones[1] / n)
# pygame.display.set_caption("NReinas ")
# marco.fill(gris)
#
# # -------- Bucle Principal del Programa  -----------
# while not hecho:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             hecho = True
#
#     ventana.tablero(prueba)
#     pygame.display.flip()
#
# pygame.quit()
#
# #=======================================FINAL DEL TOUR POR ESTA HERMOSA SOLUCION =======================================

