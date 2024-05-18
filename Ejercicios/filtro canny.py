# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:22:45 2023

@author: USUARIO
"""

import cv2
import numpy as np

#Obtenemos la foto, es necesario que sea en blanco y negro (el valor 0).
'''0: abrir la imagen en blanco y negro.
   1: abrir la imagen en color. Por defecto en esta.'''
image=cv2.imread('..\Fotos\planet_glow.jpg',0)

#Aplicamos el filtro.
bordes=cv2.Canny(image,100,200)
#Mostramos la nueva foto.
cv2.imshow('Canny',bordes)

#Cerramos la ventana.
cv2.waitKey()
cv2.destroyAllWindows()

'''Explicación valor umbrales en el filtro.
Dos umbrales: u1 y u1.
    -Si el píxel tiene un valor menor al primer umbral, x<u1, se descarta.
    -Si el píxel tiene un valo mayor al segundo umbrar, x>u2, se queda.
    -Los valores del medio solo se quedan si están contíguos a un píxel que se queda.'''