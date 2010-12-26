# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti 
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
#
# Boton Programmed by Pablo Garrido

from pilas.actores import Actor
import pilas

class Boton(Actor):
    """Representa un boton que reacciona al ser presionado."""
	
    def __init__(self, x=0, y=0):
       self.funciones_normal = []
       self.funciones_press = []
       self.funciones_over = []
       Actor.__init__(self, 'boton/boton_normal.png', x=x, y=y)
       
       pilas.eventos.mueve_mouse.conectar(self.detection_move_mouse)
       pilas.eventos.click_de_mouse.conectar(self.detection_click_mouse)
       pilas.eventos.termina_click.conectar(self.detection_end_click_mouse)
    
    #funciones que conectan evento(press, over, normal) a funciones 
    def conectar_normal(self, funcion):
        self.funciones_normal.append(funcion)
    
    def conectar_presionado(self, funcion):
        self.funciones_press.append(funcion)
    
    def conectar_sobre(self, funcion):
        self.funciones_over.append(funcion)    
    
    def desconectar_normal(self, funcion):
        self.funciones_normal.remove(funcion)
    
    def desconectar_presionado(self, funcion):
        self.funciones_press.remove(funcion)
    
    def desconectar_sobre(self, funcion):
        self.funciones_over.remove(funcion) 

    def ejecutar_funciones_normal(self):
        for i in self.funciones_normal:
            i()
    
    def ejecutar_funciones_press(self):
        for i in self.funciones_press:
            i()
    
    def ejecutar_funciones_over(self):
        for i in self.funciones_over:
            i()

    # funciones que cambian la imagen del boton
    def pintar_normal(self, ruta_normal = 'boton/boton_normal.png'):
        self.imagen_normal = pilas.imagenes.cargar(ruta_normal)
        self.definir_imagen(self.imagen_normal)

    def pintar_presionado(self, ruta_press = 'boton/boton_press.png'):
        self.imagen_press = pilas.imagenes.cargar(ruta_press)
        self.definir_imagen(self.imagen_press)

    def pintar_sobre(self, ruta_over = 'boton/boton_over.png'):
        self.imagen_over = pilas.imagenes.cargar(ruta_over)
        self.definir_imagen(self.imagen_over) 

    def detection_move_mouse(self, evento):
        if self.colisiona_con_un_punto(evento.x, evento.y):
            self.pintar_sobre()
            self.ejecutar_funciones_over()
        else:
            self.ejecutar_funciones_normal() 
            self.pintar_normal()

    def detection_click_mouse(self, click):
        if self.colisiona_con_un_punto(click.x, click.y):
            self.ejecutar_funciones_press()
            self.pintar_presionado()
            pilas.mundo.agregar_tarea(0.25, self.pintar_sobre)


    def detection_end_click_mouse(self, end_click):
        self.ejecutar_funciones_normal()
