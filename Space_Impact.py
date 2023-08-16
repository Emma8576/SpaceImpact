"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Lenguaje: Python 3.10.10
Autor: Emmanuel Eliécer Calvo Mora (2023213365)
Versión: 1.1
Fecha de última modificación:
23/04/2023
"""

#Se reliza la importación de las bibliotecas
from tkinter import *
import random
import tkinter as tk
import os
import glob
from threading import Thread
import time
import pygame
import pygame.mixer

#se crea la lista enemigo para almacenar los enemigos aleatorios que se van a aparecer en la pantalla
enemigo = []
#Recibe rutas de imagenes
def cargarimgs(input, listaResultado): #Funcion que carga las imagenes en una lista
    """
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Lenguaje: Python 3.10.10
Autor: Arturo Acuña
Descripción: Función para cargar imagenes en una lista
Entradas: Imagenes a enlistar
Salidas: Lista de imágenes
Profesor: Milton Villegas Lemus
Versión: 1.1
Fecha de última modificación:
05/04/2023
    """
    if (input == []):   #verifica si la lista de rutas está vacía, en caso afirmativo devuelve la listaResultado con las imagenes cargadas hasta el momento
        return listaResultado
    else:
        listaResultado.append(tk.PhotoImage(file = input[0]))  #si la lista input no está vacía se carga la primera imagen de la lista y se agrega a la lista resultado
        return cargarimgs(input[1:], listaResultado) #se hace la llamada recursiva y se va recorriendo la lista, esto continua hasta que se carguen todas las imagenes

#Referencia del código de Arturo Acuña
def cargarSprites(patron): #Funcion que encuentra las imagenes en el directorio Imagenes/ y se las pasa a cargarimgs
    x = glob.glob("Imagenes/" + patron)  #se usa glob para cargar imagenes del directorio imagenes, esto devuelve una lista de rutas de archivo que coinciden con el patron
    x.sort()   #ordena la lista de rutas de archivos devuelta
    return cargarimgs(x, []) #se llama la funcion cargarimgs con la lista de rutas de archivo "x" y una lista vacía

#fución para remplazar a len()
#Obtenida de chatgpt
def lenn(N):  #se toma la secuencia de datos ya sea lista, cadena de texto etc, y devuelve la longitud
    """
      Instituto Tecnológico de Costa Rica
      Ingeniería en Computadores
      Profesor: Milton Villegas Lemus
      Versión: 1.1
      Fecha de última modificación:
      05/04/2023
      Lenguaje: Python 3.10.10
      Calcula la longitud de una secuencia de datos, como una lista o una cadena de texto.
      Entrada:
      N: secuencia de datos, numeros, cantidad de imagenes, etc.
      Salida:
      La longitud de la secuencia.
      Restricciones:
      La secuencia debe ser iterable, que se puedan recorrer sus caracteres, o elementos.
      Autor:
      ChatGpt
      Ejemplo de uso:
      lenn([1, 2, 3, 4])
      4
      lenn('Hola')
      4
      """
    if N == []:  #comprueba si la lista está vacía
        return 0
    else:
        return 1 + lenn(N[1:])  #se hace slicing de la lista, contando el primer elementoto contado y sumandolo a la secuencia restante


def display(ventana, lienzo): #Aqui se va a poner todo lo que va a aparecer en el canvas
    """***********************************************************
                  Instituto Tecnológico de Costa Rica
                        Ingenieria en Computadores
                       Taller de Programación
    Lenguaje:Python 3.10.10
    Descrición:Función principal que almacena todos las funciones, botones, controles, etc. del juego
    Autores: Varios: Emmanuel Calvo Mora, ChatGpt, Codemy, Kathie Quick, entre otros.
    Profesor:Milton Villegas Lemus.
    Fecha última modificación:23/4/2023
    Entradas: ventana y lienzo
    Salidas: Todo el contenido del juego
    *************************************************************"""

    ventana.title("Space Impact")  # titulo de la ventana
    Fondo = cargarSprites("principal00*") #Se cargan los sprites del fondo
    BG = lienzo.create_image(450, 300) #Se crean y se les da una posicion inicial a las imagenes

    def MoverFondo(i): #Se crea una funcion recursiva que anima el fondo
        """***********************************************************
                      Instituto Tecnológico de Costa Rica
                            Ingenieria en Computadores
                           Taller de Programación
        Lenguaje:Python 3.10.10
        Descrición:Función para animar el fondo de forma recursiva
        Autores: Arturo Acuña
        Profesor:Milton Villegas Lemus.
        Fecha última modificación:23/4/2023
        Entradas: Entrada del indice de la imagen actual
        Salidas: no presenta
        *************************************************************"""

        if (i >= lenn(Fondo)): #La funcion itera mientras el valor de i no sea mayor a la cantidad de fotos
            i = 0 #Si i es mayor a la cantidad de fotos, se vuelve a iniciar el contador
        lienzo.itemconfig(BG, image = Fondo[i]) #Se actualiza la imagen de fondo del lienzo
        time.sleep(0.05) #Se espera un momento  para hacer la iteración
        Thread(target = MoverFondo, args = (i + 1, )).start() #Se hace una llamada recurisva en un hilo aumentando i una unidad, para hacer una animación secuencial
        #Se inician los hilos
    Thread(target = MoverFondo, args = (lenn(Fondo) - 1,)).start() #se comienza el proceso de animación comenzando desde la ultima imagen de la lista Fondo


# """"""""""""""""""""""""""""""""""""""Nave Principal"""""""""""""""""""""""""""""""""""""""""
    global nave_img
    #Inialización de la variable para los puntajes
    global Puntaje
    Puntaje = 0  #se inicia en cero el puntaje

    rutaImgNave = r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/navePrincipal.png"   #se asigna la ruta de la imagen y se ignoran las secuencias
    #se crea la imagen de la nave principal sobre el lienzo
    naveImg = PhotoImage(file= rutaImgNave)
    nave_img = lienzo.create_image(100, 250, image=naveImg)  #Crear imagen y posición de la nave

    # se agrega la imagen del misil
    rutaDisparo = r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/misil.png"  #se ingresa la ruta de la imagen
    disparoImg = PhotoImage(file= rutaDisparo)
    disparoImg.image = disparoImg  #se usa para evitar que la imagen se elimine de la memoria cuando la variable disparoImg salga de alcance.

    # Función para que la imagen no se salga del borde y hacer que la nave no salga de la pantalla
    # Referencias gracias a:
    # Kathie Quick. (2021, 16 marzo). Python Tkinter (part 4b): Edge Reached. YouTube. https://www.youtube.com/watch?v=g5qJEJjEOa4
    def limit_borde():
        borde = lienzo.bbox(nave_img)  #se utiliza para obtener las cordenadas de la caja delimitadora de la imagen de la nave
        if borde[0] < 0:                  #Se limita el borde izquierdo para que no salga de la pantalla
            lienzo.move(nave_img, 10, 0)
        elif borde[1] < 25:               #Se limita el borde superior para que no salga de la pantalla
            lienzo.move(nave_img, 0, 10)
        elif borde[2] > 900:              #Se limita el borde derecho para que no salga de la pantalla
            lienzo.move(nave_img, -10, 0)
        elif borde[3] > 500:              #Se limita el borde inferior para que no salga de la pantalla
            lienzo.move(nave_img, 0, -10)

    # funciones que permiten el movimiento de la nave
    # referencias obtenidas de:
    #Codemy.com. (2020, 18 mayo). How To Move Images On Canvas - Python Tkinter GUI Tutorial #70. YouTube.
    #     https://www.youtube.com/watch?v=2rF8-jbTL-8

  #Mover la nave principal a la izquierda
    def left(event):
        x = -10                         #tanto x como y representan la cantidad de pixeles que se movera en horizontal o vertical respectivamente
        y = 0
        lienzo.move(nave_img, x, y)     #se mueve la imagen
        limit_borde()                   #verifica cada vez que se mueve la nave si ha alcanzado el borde

    # Mover la nave principal a la derecha
    def right(event):
        x = 10                          #tanto x como y representan la cantidad de pixeles que se movera en horizontal o vertical respectivamente
        y = 0
        lienzo.move(nave_img, x, y)     #se mueve la imagen
        limit_borde()                   #verifica cada vez que se mueve la nave si ha alcanzado el borde

    # Mover la nave principal hacia arriba
    def up(event):
        x = 0                           #tanto x como y representan la cantidad de pixeles que se movera en horizontal o vertical respectivamente
        y = -10
        lienzo.move(nave_img, x, y)     #se mueve la imagen
        limit_borde()                   #verifica cada vez que se mueve la nave si ha alcanzado el borde

    # Mover la nave principal hacia abajo
    def down(event):
        x = 0                           #tanto x como y representan la cantidad de pixeles que se movera en horizontal o vertical respectivamente
        y = 10
        lienzo.move(nave_img, x, y)     #se mueve la imagen
        limit_borde()                   #verifica cada vez que se mueve la nave si ha alcanzado el borde


    #crear la etiqueta de los puntajes
    puntaje_label = Label(ventana, text= "Su Puntaje: " + str(Puntaje), bg= "black", font=("Helvetica",20), fg= "white")
    #le da ubicación a la etiqueta
    puntaje_label.place(x=100, y=10)

    # funciones para hacer el disparo del cohete
    #Referencias por:
    #Kathie Quick. (2022, 18 mayo). Python Tkinter (part 11): Shooting Projectiles. YouTube. https://www.youtube.com/watch?v=8uQ9BPD9LGo
    global disparos
    disparos = []   #Se crea una lista vacía para almacenar disparos generados

    def mover_disparo(disparo, temporizador):  #se recibe la imagen y un temporizador para controlar la recursividad
        """***********************************************************
                      Instituto Tecnológico de Costa Rica
                            Ingenieria en Computadores
                           Introducción a la Programación
        Lenguaje:Python 3.10.10
        Descrición:Función que se encarga de mover la imagen del disparo a traves de la pantalla hacia la derecha
        Autores: Kathie Quick, Emmanuel Calvo
        Profesor:Milton Villegas Lemus.
        Fecha última modificación: 23/4/2023
        Entradas: La imagen del disparo que se desea mover y el temporizador que se usa para controlar la recursividad de la función.
        Salidas:No tiene salidas, pero hace que el disparo se mueva a traves de la pantalla.
        Restricciones: La imagen del disparo, debe estar previamente cargada en la variable, disparo.
        *************************************************************"""
        try:
            lienzo.move(disparo, 100, 0)  # hace que el cohete se mueva 100 pixeles hacia la derecha
            temporizador = ventana.after(150, mover_disparo, disparo, temporizador)  # se llama a la función de forma recursiva con un tiempo de 150 milisegundos
            if lienzo.coords(disparo)[0] > 800:  # si el disparo sale de la pantalla se elimina de la pantalla y la lista disaparos
                lienzo.delete(disparo)
                disparos.remove(disparo)
                ventana.after_cancel(temporizador)
        except:
            return
    #cargar el archivo de sonido del disparo
    sonido_disparo = pygame.mixer.Sound(r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/Sdisparo.wav")
    pygame.mixer.music.play(loops=-1)
    def disparar(event):
        """***********************************************************
                             Instituto Tecnológico de Costa Rica
                                   Ingenieria en Computadores
                                  Introducción a la Programación
               Lenguaje:Python 3.10.10
               Descrición:Función que se encarga de crear y mover el misil
               Autores: ChatGpt, Emmanuel Calvo
               Profesor:Milton Villegas Lemus.
               Fecha última modificación: 23/4/2023
               Entradas: event que es un evento que desencadena la llamada a la función evento disparo
               Salidas:No tiene salidas, pero se obtienen la posición actual de la nave princiapal
               se calcula el centro de la nave para crear el misil y posteriormente se llama mover_disparo
               para disparar el misil.
               Restricciones: La imagen de disparoImg debe ser previamente cargada.
               *************************************************************"""
        global disparo
        nave_limit = lienzo.bbox(nave_img)  #se obtiene la posición  en coordenadas de la nave principal
        centro_dere_izqui = (nave_limit[0] + nave_limit[2]) / 2   #se calcula el centro de la nave en el eje horizontal
        centro_arriba_abajo = (nave_limit[1] + nave_limit[3]) / 2 #se calcula el centro de la nave en el eje vertical
        disparo = lienzo.create_image(centro_dere_izqui, centro_arriba_abajo, image=disparoImg) #se crea la imagen del "misil en el centro de la nave"
        disparos.append(disparo)  #se añade el "misil" a la lista disparos
        mover_disparo(disparo, None) #se llama a la función de mover_disparo para mover el disparo
        #Se reproduce el primero
        sonido_disparo.play()     #hace que el sonido de disparo se ejecute en cada vez que se dispara


    # se detectan las teclas presionadas y se le asignan a la funión respectiva
    ventana.bind("<Left>", left)
    ventana.bind("<Right>", right)
    ventana.bind("<Up>", up)
    ventana.bind("<Down>", down)
    ventana.bind("<space>", disparar)

#""""""""""""""""""""""""""""""""Enemigos"""""""""""""""""""""""""""""""""""""""""""""""""""""""

    # Cargar imágenes de los enemigos
    imagen1 = PhotoImage(file= r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/enemigo1.png")
    imagen2 = PhotoImage(file= r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/enemigo2.png")
    imagen3 = PhotoImage(file= r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/enemigo3.png")

    # Función para crear enemigos aleatorios
    def create_enemy():
        """***********************************************************
                                    Instituto Tecnológico de Costa Rica
                                          Ingenieria en Computadores
                                         Introducción a la Programación
                      Lenguaje:Python 3.10.10
                      Descrición:Función que crea enemigos aleatorios en posiciones aleatorias en el lienzo.
                      Autores: ChatGpt, Emmanuel Calvo
                      Profesor:Milton Villegas Lemus.
                      Fecha última modificación: 23/4/2023
                      Entradas: No posee
                      Salidas: No posee
                      Restricciones: LA función depende de tres imagenes predefinidas
                      *************************************************************"""
        global enemigo
        global imagen
        # Seleccionar una imagen aleatoria
        imagen = random.choice([imagen1, imagen2, imagen3])
        # Generar coordenadas aleatorias dentro del canvas
        x = random.randint(800, 900 - imagen.width())
        y = random.randint(0, 475 - imagen.height())
        # Crear imagen en el canvas
        enemy_id = lienzo.create_image(x, y, image=imagen, anchor=NW, tag="enemy")
        enemigo.append(enemy_id)   #se agregan los enemigos generados a una lista llamada enemigo

        # Llamar a la función de forma recursiva después de 5 segundos
        #lienzo.after(5000, create_enemy)

        def mostrar_pantalla_game_over():
            # Crear la ventana principal
            # Configurar la ventana principal
            ventana.title("Game Over")
            ventana.geometry("900x450")

            # Crear el texto del mensaje
            game_over_label = tk.Label(ventana, text="Game Over", font=("Helvetica", 30), fg="white", background= "black")
            game_over_label.pack(pady=50)

            # Crear el botón de salida
            exit_button = tk.Button(ventana, text="Salir", font=("Helvetica", 20), command=ventana.quit)
            exit_button.pack(pady=50)



        #Movimiento Constante del enemigo
        dx = -2

        # Función para mover los enemigos
        def move_enemy():
            """***********************************************************
                                 Instituto Tecnológico de Costa Rica
                                       Ingenieria en Computadores
                                      Introducción a la Programación
                   Lenguaje:Python 3.10.10
                   Descrición: Su función es mover el enemigo generado aleatoriamente por el liezo de derecha a izquierda
                   Autores: ChatGpt, Emmanuel Calvo
                   Profesor:Milton Villegas Lemus.
                   Fecha última modificación: 23/4/2023
                   Entradas: la variable global enemy_id que es el id del enemigo, y la variable dx que indica la cantidad de pixeles que se
                   mueve la imagen del enemigo en cada llamada
                   Salidas:No tiene salidas, su objetivo es actualizar la posición de los enemigos
                   Restricciones: Las imágenes de los enemigos deben estar predefinidas en una lista de imágenes llamada "imagen1", "imagen2", "imagen3"
                   *************************************************************"""
            try:
                # Mover los enemigos
                lienzo.move(enemy_id, dx, 0)
                # Obtener las nuevas coordenadas de la imagen despues de moverse
                new_coords = lienzo.coords(enemy_id)

                # Si la imagen ha salido del canvas, eliminarla
                if new_coords[0] < -imagen.width(): #si la coordeda mas a la izquierda de la imagen es menor que el ancho de la imagen se elimina la imagen
                    lienzo.delete(enemy_id)

                    # Llamar a la función para mostrar la pantalla de Game Over
                    mostrar_pantalla_game_over()
                else:
                    # Llamar a la función de forma recursiva después de 20 milisegundos
                    lienzo.after(20, move_enemy)
            except:
                pass
        # Llamar a la función de movimiento
        move_enemy()
        # Llamar a la función de forma recursiva después de 3 segundos
        lienzo.after(3000, create_enemy)

    # Llamar a la función para crear enemigos aleatorios
    create_enemy()

#Función que recorre la lista disparos
    def recorrer_enemigos(enemigo, i=0):
        """***********************************************************
                              Instituto Tecnológico de Costa Rica
                                    Ingenieria en Computadores
                                   Introducción a la Programación
                Lenguaje:Python 3.10.10
                Descrición:Función que se encarga de mover la imagen del disparo a traves de la pantalla hacia la derecha
                Autores: ChatGpt, Emmanuel Calvo
                Profesor:Milton Villegas Lemus.
                Fecha última modificación: 23/4/2023
                Entradas: Lista de enemigos, y el indice que indica la posición en la lista.
                Salidas: No devuelve ninguna
                Restricciones: La lista enemigos debe contener las imagenes con enemigos válidos en el juego.
                *************************************************************"""
        # Caso base: si i es mayor o igual a la longitud de la lista 'enemigo', se llama a 'recorrer_enemigos' de nuevo después de 150 ms y se sale de la función
        if i >= lenn(enemigo):
            ventana.after(150, recorrer_enemigos, enemigo)
            return
        print("Recorre lista enemigo")
        # Llama a 'recorrer_disparos' con la lista 'disparos' y el índice 'i'
        recorrer_disparos(disparos, i)
        # Llama a 'recorrer_enemigos' de nuevo con el índice incrementado en 1
        recorrer_enemigos(enemigo, i + 1)

        # Función que recorre la lista disparos
    def recorrer_disparos(disparos, i, j=0):
        """***********************************************************
                              Instituto Tecnológico de Costa Rica
                                    Ingenieria en Computadores
                                   Introducción a la Programación
                Lenguaje:Python 3.10.10
                Descrición: Recorre la lista de disparos y llama a la función choque enemigo para cada disapro
                en la lista, usando el indice i para cada enemigo en la lista.
                Autores: ChatGpt, Emmanuel Calvo, Ramsés Gutierrez
                Profesor:Milton Villegas Lemus.
                Fecha última modificación: 23/4/2023
                Entradas: disparos: lista de disparos, indice i que indica la posición en que se encuentra la función
                j: indice que indica la posición de la función en la lista de disparos
                Salidas: No devuelve ninguna
                Restricciones: Los índices 'i' y 'j' deben ser números enteros no negativos que no excedan el número de
                 elementos en las listas 'enemigo' y 'disparos', respectivamente.
                *************************************************************"""
        # Caso base: si j es mayor o igual a la longitud de la lista 'disparos', se sale de la función
        if j >= lenn(disparos):
            return
        # Llama a 'choque_enemigo' con los índices 'i' y 'j'
        choque_enemigo(i, j)
            # se llama de nuevo la función
        print("recorre lista disparos", j)
        recorrer_disparos(disparos,i , j + 1) #se recorre la lista  al siguiente disparo

    #se realiza la detección de colision entre el misil y el enemigo
    def choque_enemigo(i, j):
        """***********************************************************
                                     Instituto Tecnológico de Costa Rica
                                           Ingenieria en Computadores
                                          Introducción a la Programación
                       Lenguaje:Python 3.10.10
                       Descrición: Recorre la lista de disparos y llama a la función choque enemigo para cada disapro
                       en la lista, usando el indice i para cada enemigo en la lista.
                       Autores: ChatGpt, Emmanuel Calvo, Ramsés Gutierrez
                       Profesor:Milton Villegas Lemus.
                       Fecha última modificación: 23/4/2023
                       Entradas: El indice i y j que corresponden al indice del enemigo y el misil respectivamente.
                       j: indice que indica la posición de la función en la lista de disparos
                       Salidas: No devuelve ningun valor,pero modifica las variables globales, disparos, enemigo y Puntaje.
                       Restricciones: Las variables disparos, enemigo, Puntaje y nave_img deben estar definidas y ser globales.
                       *************************************************************"""


        global disparos, enemigo, Puntaje, nave_img
        try:
            print("Ingresa a la función de choque")

            borde_misil = lienzo.bbox(disparos[j])  #se obtiene las coordenadas de cada misil
            borde_enemigo = lienzo.bbox(enemigo[i]) #se obtienen las coordenadas de cada enemigo
            #si las coordenadas de las cajas delimitadoras se superponen en los ejes x e y se asume que hay colisión entre el misil y el enemigo
            if (borde_misil[0] < borde_enemigo[2] and borde_misil[2] > borde_enemigo[0] and
                borde_misil[1] < borde_enemigo[3] and borde_misil[3] > borde_enemigo[1]):

                #Se carga el sonido de la explosión
                sonido_explosion = pygame.mixer.Sound(r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/explosion.wav")
                # Establecer el volumen a 0.3
                sonido_explosion.set_volume(0.3)
                #se le inicializa el sonido de la explosión
                sonido_explosion.play()
                Puntaje +=100   #Se aumenta el puntaje si hay colisión
                puntaje_label.config(text= " Su Puntaje: " + str(Puntaje))
                #este fragmnto se encarga de eliminar los elementos visualmete de la pantalla además de actualizar las listas que los almacenen
                lienzo.delete(disparos[j])  #elimina la imagen del misil
                disparos = disparos[:j] + disparos[j+1:] #actualiza la lista de disparos eliminando el misil que colisionó
                lienzo.delete(enemigo[i])  #elimina la imagen del enemigo del lienzo
                enemigo = enemigo[:j] + enemigo[j+1:]  #actualiza la lista de enemigos eliminando el enemigo que colisionó
                print("Hubo colisión")
            else:
                # no hay colisión: se continúa con la ejecución del programa
                pass
            return
        except:
            print("No hubo colisión")
            return
            pass

    ventana.after(150, recorrer_enemigos, enemigo)   #se llama a la función recorrer_enemigos y enemigo para recorrer la lista y ver si hay nuevas colisiones


    #se hace que las naves enemigas también disparen
    # se agrega la imagen del misil del enemigo
    rutaDisparoEne = r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/misilEnemigo.png"
    disparoEne = PhotoImage(file=rutaDisparoEne)
    disparoImg.image = disparoImg

    def enemy_fire3():
        """***********************************************************
                                            Instituto Tecnológico de Costa Rica
                                                  Ingenieria en Computadores
                                                 Introducción a la Programación
                              Lenguaje:Python 3.10.10
                              Descrición: crea un objeto de disparo para el enemigo y lo mueve hacia la posición del jugador
                               en el canvas. También llama a sí misma después de un segundo para que el enemigo pueda volver a disparar.
                              Autores: ChatGpt, Emmanuel Calvo
                              Profesor:Milton Villegas Lemus.
                              Fecha última modificación: 23/4/2023
                              Entradas: no hay entradas en la función
                              Salidas: Esta función no tiene una salida, sino que se encarga de crear y mover objetos en el canvas.
                              Restricciones: Esta función asume que hay un objeto de enemigo y una imagen de disparo llamada disparoEne creados previamente en el canvas.
                              *************************************************************"""

        # crea un objeto para el disparo del enemigo en la posición del enemigo
        enemy_shot = lienzo.create_image(lienzo.coords(enemigo), image=disparoEne)

        # mueve el disparo hacia la posición de la nave del jugador cada 10 milisegundos
        def move_shot3():
            if lienzo.coords(enemy_shot)[0] > 0: #se verifica que no haya salido de la pantalla
                lienzo.move(enemy_shot, -10, 0)    #se mueve el misil hacie el jugador
                lienzo.after(10, move_shot3)       # se vuelve a llamar a la función cada 10 milisegundos
            else:
                lienzo.delete(enemy_shot)

        move_shot3()
        # llama a enemy_fire() nuevamente después de 1 segundos (1000 milisegundos) para que la nave vuelva a disparar
        lienzo.after(1000, enemy_fire3)

    enemy_fire3()



    ventana.mainloop()
    #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


