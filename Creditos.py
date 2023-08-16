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
import tkinter as tk

#destruye la lista de elementos para cambiar de pantalla.
def destruirLista(List): # Esta funcion borra lo que esta en el canvas de manera recursiva
    if List == []: #Condicion de finalizacion
        return []
    else:
        (List[0]).destroy() #Se destruye el primer elemmento
        return destruirLista(List[1:]) #Se hace slicing de la lista


#función que muestra en la ventana de créditos los detalles de la universisad, autor y juego.
def displayCreditos(ventana,lienzo):
    lista_temp = []
    creditosLabel = tk.Label(ventana, text="Instituto Tecnológico de Costa Rica\nCarrera: Ingeniería en Computadores\nCurso: Taller de Programación\nProfesor: Milton Villegas Lemus\n Autor: Emmanuel Eliécer Calvo Mora\nCarnet: 2023213365\nPaís de Origen: Costa Rica\nVersión del Juego: 1.1\nAño de creación: 2023", font=("Helvetica", 15, "bold"), fg="white",
                               background="black", activebackground="gray", activeforeground="white", bd=10)
    creditosLabel.pack(pady=30)
    lista_temp.append(creditosLabel)
    ruta_autor = PhotoImage(file= r"C:\Users\Emmanuel\Desktop\Proyecto1\Imagenes/autor.png")
    imagen_autor = lienzo.create_image(450, 350, anchor = "center", image = ruta_autor)
    lista_temp.append(imagen_autor)

    botonSalir = tk.Button(ventana, width=10, height= 2, text= "Atrás",font=("Arial", 11, "bold"), command= "", fg="white", background="black", activebackground="gray", activeforeground="white", bd=10) # se crea el botón de Salir del juego
    botonSalir.place(x = 0, y = 0, anchor= "nw" ) # ubicación de boton de Atrás
    lista_temp.append(botonSalir)
    ventana.mainloop()

