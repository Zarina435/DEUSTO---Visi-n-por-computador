# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:19:21 2023

@author: USUARIO
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Obtenemos la imagen.
img = cv2.pyrDown(cv2.imread('..\Fotos\gorka.jpeg', cv2.IMREAD_UNCHANGED))

#Obtenemos contornos.
bordes=cv2.Canny(img,90,255)
ret, thresh = cv2.threshold(bordes,0,255,cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 
#Obtenemos el mayor contorno y su rectangulo.
c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
rect =(x,y,w,h)

cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

#Creamos una mascara de inicio
mascara = np.zeros(img.shape[:2], np.uint8)

#Creamos las matrices que utilizara grabcut.
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

#Aplicamos grabcut al frame video utilizando el rectangulo
cv2.grabCut(img, mascara, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)

#Creamos una mascara binaria, los pix etiquetados como probable piel (2), seguro son piel (3)
mascara2 = np.where((mascara == 2) | (mascara == 0), 0, 1).astype('uint8')

#Aplicamos la mascara al frame
piel_detectectada = img * mascara2[:, :, np.newaxis]

plt.subplot(121)
plt.imshow(cv2.cvtColor(piel_detectectada, cv2.COLOR_BGR2RGB))
plt.title("grabcut")
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.xticks([])
plt.yticks([])
plt.show()
