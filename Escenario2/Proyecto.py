#-------------------------------------------------------------------------------
# Name:Proyecto simulacion
# Purpose:
#
# Author:      Stiveen Correa 1556134
#              Alvaro Javier Quintero 1556009
#              Kevin Santiago Lemos 1556
#
# Created:     21/08/2019
# Copyright:   (c) Stiveen13 and JF 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#LIBRERIAS
import random
import simpy
import numpy
import time
from timeit import timeit
import LasVegas
import NReinas

#Datos de la simulación
SEMILLA = random.seed(0) #Semilla generador
LLEGADA_CLIENTES =random.uniform(10,30)
COLA = 0
MAX_COLA = 0
ESPERA_CLIENTES = numpy.array([])
UTILIDAD = 0
utilidad_gana = 15
utilidad_pierde = -10
partidas_ganadas=0
partidas_perdidas=0
total_partidas=0


#FUNCION RANDOM PROBABILIDAD PONDERADA
#opciones = [( 4, 10),( 5, 10),(6, 10), (8, 10),(9,10),(10,10),(12,10),(14,10),(15,10)]
opciones=[4,5,6,7,8,9,10,11,12,13,14,15]

#fUNCION LLEGADA
def llegada(env, serv):
    i = 0
    while True:

        i= i+1
        c = cliente(env, 'Partida %02d' % i, serv)
        env.process(c)
        tiempo_llegada =random.uniform(5,15) #se cambia este parametro para este escenario, los robots llegan mas rapido
        yield env.timeout(tiempo_llegada) #Yield retorna un objeto iterable
        #HASTA  QUE TIEMPO DE LA SIMULACION DEBO LLEGAR
        if(env.now>28800):
            break





#FUNCION CLIENTE
def cliente(env, nombre, servidor):
    #El cliente llega y se va cuando es atendido
    llegada = env.now
    print('%7.2f'%(env.now)," Se inicia la partida  ", nombre)
    global COLA
    global MAX_COLA
    global ESPERA_CLIENTES
    global UTILIDAD
    global partidas_ganadas
    global partidas_perdidas
    global total_partidas
    #Atendemos a los clientes (retorno del yield)
    #With ejecuta un iterador sin importar si hay excepciones o no
    with servidor.request() as req:

		#Hacemos la espera hasta que sea atendido el cliente
        COLA += 1
        if COLA > MAX_COLA:
            MAX_COLA = COLA

		#print("Tamaño cola", COLA)
        results = yield req
        COLA = COLA - 1
        espera = env.now - llegada
        ESPERA_CLIENTES = numpy.append(ESPERA_CLIENTES, espera)
        print('%7.2f'%(env.now), " El cliente ",nombre," espera a ser atendido ",espera)

        opcion_cliente = random.choice(opciones)
        tiempo_atencion_Profesor= 0
        tiempo_atencion_Robot= 0
        start_time_Robot =time.time()
        LasVegas.hastaQueTermine(opcion_cliente)
        tiempo_deejcucion_Robot =time.time()
        tiempo_atencion_Robot =tiempo_deejcucion_Robot - start_time_Robot

        start_time_Profesor =time.time()
        NReinas.nReiansSolver(opcion_cliente)
        tiempo_deejcucion_Profesor =time.time()
        tiempo_atencion_Profesor =tiempo_deejcucion_Profesor - start_time_Profesor

        if(tiempo_atencion_Profesor < tiempo_atencion_Robot):
            UTILIDAD += utilidad_gana
            partidas_ganadas += 1
            yield env.timeout(tiempo_atencion_Profesor)

        else:
            UTILIDAD += utilidad_pierde
            partidas_perdidas += 1
            yield env.timeout(tiempo_atencion_Robot)

#        print('%7.2f'%(env.now), " Sale el cliente ",nombre)

        print('%7.2f'%(env.now), " Partida numero",nombre)
        total_partidas=nombre



#Inicio de la simulación

print('Carlitos VS Maquina')
random.seed(SEMILLA)
env = simpy.Environment()

#Inicio del proceso y ejecución
#pARTIDA
servidor = simpy.Resource(env, capacity=2)
env.process(llegada(env, servidor))
env.run()

print("Cola máxima ",MAX_COLA)
print("Tiempo promedio de espera ",'%7.2f'%(numpy.mean(ESPERA_CLIENTES)))
print("La utilidad  ganada por Carlitos fue : ", UTILIDAD)
print("las partidads ganadas por profesor",partidas_ganadas)
print("las partidas  perdidas por el profesor  fueron ", partidas_perdidas)
print("Numero de partida alcanzada ===> ",total_partidas)