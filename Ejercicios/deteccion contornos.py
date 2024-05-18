# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:38:20 2023

@author: USUARIO
"""

import cv2
import numpy as np


#---------------------------CON UN CUADRADO------------------------------------
#Creamos una nueva imagen como un numpy array.
image=np.zeros((200,200),dtype=np.uint8)
#Creamos un cuadrado.
image[50:150,50:150]=255

'''Función que binariza. Los parámteros son: imagen que se quiere binarizar, 
con el que se binariza (nos quedams con esos píxeles). la intensidad de los
píxeles que cumplan el primer umbral (blanco 255) y los píxeles con los que 
queremos quedarnos (2 es para quedarnos con lo superior al umbral).'''
ret,thresh=cv2.threshold(image,127,255,0)

#Obtenemos los contornos de las siluetas.
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Pasamos la foto a RGB.
color=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
#Dibuja el contorno en verde.
image=cv2.drawContours(color,contours,-1,(0,255,0),2)

#Mostramos la nueva imagen.
cv2.imshow("Contornos",color)

#---------------------------CON FOTO PLANETAS----------------------------------
#Abrimos la foto.
image=cv2.imread('..\Fotos\planet_glow.jpg',0)

#Binarizamos y obtenemos las siluetas..
ret,thresh=cv2.threshold(image,25,255,0)

#Obtenemos los contornos de las siluetas. El segundo parámetro es cómo devuelve las jerarquías.
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,1)
#Pasamos la foto a RGB (estaba en blanco y negro).
color=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
#Dibuja el contorno con el color que se indique.
image=cv2.drawContours(color,contours,-1,(255,255,0),2)

#Mostramos la nueva imagen.
cv2.imshow("Contornos",color)

#Cerramos la ventana.
cv2.waitKey()
cv2.destroyAllWindows()
