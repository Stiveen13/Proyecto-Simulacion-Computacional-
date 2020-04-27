"""

Clase Interfaz:
Clase encargada de la interfaz de la simución del problema

Alvaro Javier Quintero Peña - 201556009
Kevin Santiago Lemos López - 201556168
Stiveen Correa Escobar - 201556134

"""
import pygame



#Función para pintar la matriz solucion con las reinas posicionadas
def pintarSolucion(Reinas,n):
    #n = 8
    print("esto es ",n)
    for i in range (n):
        for j in range (n):
            print(Reinas[i][j], end=" ")
        print("\n")
    return Reinas

#Funcion que se asegura que se pueda colocar una reina
def mePuedoPoner(Reinas, f, c,n):
    #n=8
    #valida fila hacia la izquierda
    for i in range (c):
        if (Reinas[f][i] == 1):
            return False

    #Valida diagonal izquiera arriba
    #for (i = row, j = col; i >= 0 && j >= 0; i--, j--)

    #for i in range(f): #and for j in range(c, -1, -1):
    for i,j in zip(range(f, -1, -1), range (c, -1, -1)):
        if Reinas[i][j] == 1 :
            #print("mesali1")
            #print(Reinas)
            return False

    #for i  in range(f, n), j in range
    #for (i = row, j = col; j >= 0 && i < N; i++, j--)
    # Valida diagonal izquiera abajo
    for i, j in zip(range(f, n), range(c, -1, -1)):
        if Reinas[i][j] == 1:
            #print("mesali2")
            #print(Reinas)
            return False

    return True

#funcioón recursiva para resolver las n reinas
def nReinasSolucionador(Reinas, c,n):
    #Caso final: si las n reinas están puestas retorna True
    if c >= n:
        return True

    #Toma esta columna e intenta colocar una reina en todas
    #las filas una por una
    for i in range(n):
        #mira si la reina puede ser colocada en Reinas[i][c]
        if (mePuedoPoner(Reinas, i, c,n)):
            #Pone la reina en Reina[i][c]
            Reinas[i][c] = 1

            #Recure a poner el resto de la reinas
            if (nReinasSolucionador(Reinas, c + 1,n) == True):
                return True

            #Si poner la reina en el Reinas[i][c] no lleva a una solución,
            #entonces se retira la reina
            """Backtrack"""
            Reinas[i][c]=0

    return False

def tableroNxN(n):
    aux = []
    tab = []
    for i in range (n):
        aux.append(0)

    for i in range(n):
        tab.append(aux)

    print(tab)
    return tab

#tableroNxN()


#Esta función resuleve el problema de las n reinas por medio de Backtracking,
#usa principalmente nReinasSolucionador() para dar solución al problema,
#retorna falso si la reina no puede ser colocada en algua posición,
#de ser otro caso, retorna verdadero y pone la reina en forma de 1


#definimos nuestras piesas
#cuadros del tablero
def pintar (vec, x):
    gris = (183, 133, 77 )
    amarillo = (240, 144, 36 )
    Gris=pygame.image.load("gris.png")
    Amarillo=pygame.image.load("amarillo.png")

    #se pide el tamaño del tablero a solucionar
    n=x

    #cargamos la imagen de png fe la reina
    reina=pygame.image.load("reina.png")

    #se define el arreglo con el que pintará el tablero
    prueba=vec
    print("SOY PRUEBAAAAAAAAAAAAAAAAAAAAAAAAAAAA", prueba)
    #prueba=[[0,2,0,-1],[-1,0,-1,0],[2,-1,0,-1],[-1,0,-1,2]]

    #Clase ventana para mostar la interfaz
    class ventana:
        def tablero (matrix):
           i=0
           print(len (matrix))
           for l in range(len(matrix)):
               print("soy l",i)
               j=0
               for k in range(len(matrix)):
                if(matrix[l][k]==-10): #si es -10 se pinta amarillo
                    marco.blit(Amarillo,(i,j))
                   #pygame.draw.rect(marco, amarillo, [j, i, 36, 36], 0)
                    j+=36
                    #print("amarillo")
                elif(matrix[l][k]==0): #si es 0 se pinta balco
                    marco.blit(Gris,(i,j))
                     #pygame.draw.rect(marco, gris, [j, i, 36, 36], 0)
                        #print("girs")
                    j+=36
                else:
                    marco.blit(reina,(i,j)) #en otro caso se pone la reina
                        #print("reina")
                    j+=36
               i+=36
           return 0

    #inicializacion de Pygame para el tablero
    pygame.init()

    # Establecemos el alto y largo de la pantalla
    #dimensiones = [700, 500]
    #marco= pygame.display.set_mode(dimensiones)
    marco= pygame.display.set_mode(((n*36),(n*36)))
    hecho=False
    #ancho = int(dimensiones[0] / n)
    #alto = int(dimensiones[1] / n)
    pygame.display.set_caption("NReinas ")
    marco.fill(gris)

    # -------- Bucle Principal del Programa  -----------
    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

        ventana.tablero(prueba)
        pygame.display.flip()

    pygame.quit()



def nReiansSolver(n):

    #Creamos el tablero de tamaño n*n max 15 -> 15 * 15
    rn = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #rn = tableroNxN()

    if (nReinasSolucionador(rn, 0,n) == False):
        print("No haber solución")
        return False

    #pintarSolucion(rn,n)
    #pintar(rn, n)
    return True

#p = int(input("ingrese el numero de reinas"))
#nReiansSolver(p)
