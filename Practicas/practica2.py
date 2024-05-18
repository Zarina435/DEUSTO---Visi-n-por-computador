
import cv2
import numpy as np

#Capturamos con la cámara interna.
cameraCapture = cv2.VideoCapture(0)

#Capturamos primer fotograma.
success, frame = cameraCapture.read()

#Nombramos la ventana que va a abrirse.
cv2.namedWindow('MyWindow')
#Bucle paa capturar fotogramas.
while success:
    #Aplicamos un filtro de paso bajo.
    dst = cv2.GaussianBlur(frame, (7,7), 10)

    #Crear máscara.
    mask = cv2.inRange(dst, (20, 52, 90), (130, 190, 220))
    #Aplicamos máscara.
    result = cv2.bitwise_and(frame, frame, mask=mask)
    #Mostramos la ventana con el frame.
    
    cv2.imshow('MyWindow', result)
    #Capturamos el siguiente frame.
    success, frame = cameraCapture.read()

#Cerramos la ventana al terminar.
cv2.destroyWindow('MyWindow')
#Liberamos la cámara al terminar.
cameraCapture.release()