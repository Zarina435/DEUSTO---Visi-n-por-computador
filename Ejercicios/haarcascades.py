# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:35:27 2023

@author: USUARIO
"""

import cv2

#Cargamos el xml del clasificador.
face_cascade = cv2.CascadeClassifier('..\haarcascades\haarcascade_frontalface_default.xml')

#Leemos la imagen.
img = cv2.imread('..\Fotos\woodcutters.jpg')
#Pasamos la imagen a blanco y negro.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detección de caras.
faces = face_cascade.detectMultiScale(gray, 1.08, 5)

#Para cada cara detectada, pintamos el rectángulo.
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
#Mostramos la imagen.
cv2.namedWindow('Woodcutters Detected!')
cv2.imshow('Woodcutters Detected!', img)
cv2.waitKey(0)