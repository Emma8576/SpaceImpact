"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Lenguaje: Python 3.10.10
Autor: Emmanuel Eliécer Calvo Mora (2023213365)
Versión: 1.1
Fecha de última modificación:
23/04/2023
"""

from tkinter import *
import random
import tkinter as tk
import Space_Impact
global ventana
global lienzo



def destruirLista(List): # Esta funcion borra lo que esta en el canvas de manera recursiva
    if List == []: #Condicion de finalizacion
        return []
    else:
        (List[0]).destroy() #Se destruye el primer elemmento
        return destruirLista(List[1:]) #Se hace slicing de la lista

def displayDificultades(ventana, lienzo):
    global lista_temp

    def inicioJuego():
        destruirLista(lista_temp)  # se borran los elementos en pantalla
        # Crear imagen

        # Crear barra de progreso
        progress_canvas = tk.Canvas(lienzo, width=300, height=20, bg="white") #se crea la barra sobre el lienzo
        progress_canvas.place(x=450, y=400, anchor="center")
        progress_bar = progress_canvas.create_rectangle(0, 0, 0, 20, fill="blue") #se crea un rectangulo sobre el lienzo

        # Función recursiva para actualizar la barra de progreso
        def update_progress(progress):
            if progress >= 100:
                # Cerrar la barra de progreso cuando termine de cargarse el juego
                progress_canvas.destroy()
                Space_Impact.display(ventana, lienzo)  # abre la ventana del juego

            else:
                # Actualizar el tamaño de la barra de progreso
                progress_canvas.coords(progress_bar, 0, 0, progress * 3, 20)
                ventana.after(100, update_progress, progress + 1) #se programa la llamada recursiva despues de 100 milisegundos y progress + 1, es para aumentar el progreso en cada iteracion

        # Iniciar la función recursiva para actualizar la barra de progreso
        update_progress(0)

    lista_temp = []
    difficulty_label = tk.Label(ventana, text="Seleccionar dificultad", font=("Arial", 20, "bold"), fg="white", background="black", activebackground="gray", activeforeground="white", bd=10)
    difficulty_label.pack(pady=30) #colocar la etiqueta en el lienzo con un relleno de 30 pixeles por encima y debajo del widget
    lista_temp.append(difficulty_label)
    # Crear los botones para las diferentes dificultades
    easy_button = tk.Button(ventana, text="Fácil", font=("Arial", 11, "bold"),fg="white", background="black", activebackground="gray", activeforeground="white", bd=10, command= inicioJuego)
    easy_button.pack(pady=30)
    lista_temp.append(easy_button)

    medium_button = tk.Button(ventana, text="Intermedio",font=("Arial", 11, "bold"),fg="white", background="black", activebackground="gray", activeforeground="white", bd=10,
                              command=inicioJuego)
    medium_button.pack(pady=30)
    lista_temp.append(medium_button)
    hard_button = tk.Button(ventana, text="Difícil", font=("Arial", 11, "bold"), fg="white", background="black", activebackground="gray", activeforeground="white", bd=10, command=inicioJuego)
    hard_button.pack(pady=30)
    lista_temp.append(hard_button)

    ventana.mainloop()