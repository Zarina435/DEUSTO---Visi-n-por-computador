import cv2
import math
import numpy as np

#Leemos la imagen.
image=cv2.imread('..\Fotos\planet_glow.jpg')

#Cogemos las características.
alto,ancho,canales=image.shape

#Definir fecuencia, amplitud y fase de la onda del coseno.
frecuencia=5
amplitud=200
fase=0

#Pintamos el coseno.
for i in range(0,ancho):
    cos=int(amplitud+np.cos(2*np.pi*frecuencia*i/ancho+fase))+alto//2
    image[i,cos]=[255,255,255]
    
#Vemos la nueva imagen.
cv2.imshow('planetas_diagonal',image)
cv2.waitKey(0)