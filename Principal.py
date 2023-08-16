"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Lenguaje: Python 3.10.10
Autor: Emmanuel Eliécer Calvo Mora (2023213365)
Versión: 1.1
Fecha de última modificación:
23/04/2023
"""
#se importan las librerías necesarias
from tkinter import *
import tkinter as tk
import Mejores_Puntajes
import Creditos
import Dificultades
import Space_Impact
import pygame
import pygame.mixer
#Módulo para crear la música
pygame.mixer.init()
#constantes del tamaño de la ventana
WIDTH = 900
HEIGHT = 500

def destruirLista(List): # Esta funcion borra lo que esta en el canvas de manera recursiva
    if List == []: #Condicion de finalizacion
        return []
    else:
        (List[0]).destroy() #Se destruye el primer elemmento
        return destruirLista(List[1:]) #Se hace slicing de la lista
#se crea la ventana principal
#se ajusta el tamaño
global ventana

ventana = Tk()
ventana.geometry("900x500+200+80") #se genera la ventana con la medida y la ubicación deseada
ventana.resizable(False, False)  #se impide la modificación del tamaño
ventana.title("Menú Principal")  #se agrega el titulo al menú principal

def menu_principal(): #se crea la pantalla inicial del juego

    """***********************************************************
                  Instituto Tecnológico de Costa Rica
                        Ingenieria en Computadores
                       Introducción a la Programación
    Lenguaje:Python 3.10.10
    Descrición:Funcion principal de la pantalla de inicio, muestra todos los botones y etiquetas
    Autores: Arturo Acuña, Emmanuel Calvo Mora.
    Profesor:Milton Villegas Lemus.
    Fecha última modificación: 23/4/2023
    Entradas: Ninguna
    Salidas:no hay salidas explicitas, pero se muestran cambios en la pantalla incluyendo botones, etiquetas, etc.

    *************************************************************"""

    pygame.mixer.music.load(r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/juegoS.wav")   #se carga el audio
    pygame.mixer.music.play(loops=-1)  #se reproduce en bucle infinito

    #se posiciona un objeto en el centro horizontal y vertical respectivamente
    x = WIDTH/2
    y = HEIGHT/2
    # se crea el lienzo donde van los elementos
    global lienzo
    lienzo = Canvas(ventana, width= WIDTH, height= HEIGHT)
    lienzo.place(x=0, y=0)  #se le da posición al lienzo
 #se carga la imagen del fondo
    rutaImgFondoP = r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/FondosP.png"
    FondoPImg = PhotoImage(file=rutaImgFondoP) #Se carga la imagen
    FondoPImg = FondoPImg.subsample(2, 2)  #se reduce el tamaño a la mitad de la imagen
    img_Fondo = lienzo.create_image(0, 0, anchor="center", image=FondoPImg)  #se crea la imagen sobre el lienzo

    lista_temp = [] # se agragarán los elementos de la pantalla para su posterior eliminación

#Se crea la etiqueta de Bienvenida de la pantalla inicial

    etiquetaBienvenido = tk.Label(lienzo, text= "Bienvenido", font= ("Arial", 40), fg= "white", background= "black" ) # se crea la etiqueta de bienvenida
    etiquetaBienvenido.place(x = 450, y = 50, anchor = "center") # Se le asigna una ubicación a etiqueta de bienvenida
    lista_temp.append(etiquetaBienvenido)

#funciones que se ejecutarán cuando se presione el botón
#funciones para cambiar de pantalla
#autor: Arturo Acuña

    def dificultades():
        destruirLista(lista_temp) #se borran los elementos en pantalla
        Dificultades.displayDificultades(ventana, lienzo) #abre la ventana de mejores puntajes

    def pantallaPuntaje():
        destruirLista(lista_temp) #se borran los elementos en pantalla
        Mejores_Puntajes.displayPuntaje(ventana, lienzo) #abre la ventana de mejores puntajes

    def pantallaCreditos():

        destruirLista(lista_temp)  # se borran los elementos en pantalla
        Creditos.displayCreditos(ventana, lienzo)  # abre la ventana de mejores puntajes
#Se crean los botones de la pantalla principal

    botonInicio = tk.Button(lienzo, width=15, height=5, text= "Iniciar el Juego", font=("Arial", 12, "bold"), command= dificultades, fg="white", background="black", activebackground="gray", activeforeground="white", bd=10) # se crea el botón de inicio del juego
    botonInicio.place(x = 450, y = 300, anchor= "center" ) # ubicación de boton de inicio
    lista_temp.append(botonInicio) #se agrega a la lista para destruirlo luego

    botonPuntaje = tk.Button(lienzo, width= 15, height= 3, text= "Mejores Puntajes", font=("Arial", 11, "bold"), command= pantallaPuntaje, fg="white", background="black", activebackground="red", activeforeground="white", bd=10) # se crea el botón de puntajes
    botonPuntaje.place(x = 225, y = 300, anchor= "center" ) # ubicación de boton de puntajes
    lista_temp.append(botonPuntaje) #se agrega a la lista para destruirlo luego

    botonCreditos = tk.Button(lienzo, width=15, height= 3, text= "Créditos",font=("Arial", 11, "bold"), command= pantallaCreditos, fg="white", background="black", activebackground="red", activeforeground="white", bd=10) # se crea el botón de créditos
    botonCreditos.place(x = 675, y = 300, anchor= "center" ) # ubicación de boton de créditos
    lista_temp.append(botonCreditos) #se agrega a la lista para destruirlo fluego

    botonSalir = tk.Button(ventana, width=10, height= 2, text= "Salir",font=("Arial", 11, "bold"), command= ventana.quit, fg="white", background="black", activebackground="gray", activeforeground="white", bd=10) # se crea el botón de Salir del juego
    botonSalir.place(x = 0, y = 0, anchor= "nw" ) # ubicación de boton de Salir
    lista_temp.append(botonSalir) #se agrega a la lista para destruirlo luego


    ventana.mainloop() #Se usa para mantener actualizada la pantalla

menu_principal() #Se llama a la función principal para que muestretodo en la ventana