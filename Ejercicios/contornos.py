import cv2
import numpy as np

#Abrimos la imagen.
img=cv2.pyrDown(cv2.imread('..\Fotos\planet_glow.jpg',cv2.IMREAD_UNCHANGED))

#Aplicamos un filtro.
ret,thresh=cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
#Obtenemos los contornos.
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Para cada uno de los contornos.
for c in contours:
    '''
    #Encontrar las coordenadas del cuadrado delimitador.
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    #Encontrar el área mínima
    rect = cv2.minAreaRect(c)
    #Calcular las coordenadas del rectángulo de área mínima
    box = cv2.boxPoints(rect)
    #Normalizar las coordenadas a enteros
    box = np.int0(box)
    #Dibujar contornos
    cv2.drawContours(img, [box], 0, (0,0, 255), 3)
    
    #Calcular el centro y radio del circulo mínimo
    (x, y), radius = cv2.minEnclosingCircle(c)
    #Cast a enteros
    center = (int(x), int(y))
    radius = int(radius)
    #Dibujar el círculo
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)'''
    '''
    #Para el área.
    area=cv2.contourArea(c)
    
    #Aproximación.
    epsilon=0.1*cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,epsilon,True)
    cv2.drawContours(img, [approx], -1, (255, 255, 255), 1)'''
    
    #Información adicional.
    hull = cv2.convexHull(c)
    cv2.drawContours(img, [hull], -1, (0, 0, 255), 2)

#Dibuja todos los contornos
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
#Muestra la imagen con los contornos.
cv2.imshow("contours", img)

#Cerramos la ventana.
cv2.waitKey()
cv2.destroyAllWindows()