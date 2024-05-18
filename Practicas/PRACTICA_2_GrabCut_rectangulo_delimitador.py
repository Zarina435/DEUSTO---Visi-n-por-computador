import cv2
import numpy as np

#Capturamos el video
cap = cv2.VideoCapture(0)

while True:
    #Capturando el frame
    ret, frame = cap.read()

    #Convertimos el frame a escala de gris
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Aplicamos desenfoque gausiano para reducir ruido
    blurred = cv2.GaussianBlur(gris, (5, 5), 0)

    #Aplicamos Canny para detectar bordes
    bordes = cv2.Canny(blurred, 50, 150)

    #Buscamos los contornos en los bordes que detecta canny
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Buscamos el contorno mas grande que correspondera a la persona en la imagen
    if contornos:
        maximocontorno = max(contornos, key=cv2.contourArea)

        #Sacamos las coordenadas del rectangulo delimitador con contorno mas grande
        x, y, w, h = cv2.boundingRect(maximocontorno)

        #Creamos la mascara
        mascara = np.zeros(frame.shape[:2], np.uint8)
        #Matrices que utiliza GrabCut
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        #Aplicamos GrabCut al frame utilizando el rectangulo delimitador
        cv2.grabCut(frame, mascara, (x, y, x + w, y + h), bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

        #Creamos la mascara binaria, los píxeles etiquetados como probable piel (2), seguro son piel (3)
        mascara2 = np.where((mascara == 2) | (mascara == 0), 0, 1).astype('uint8')

        #Aplicamos la mascara al frame
        piel_umbralizada = frame * mascara2[:, :, np.newaxis]

        #Mostrar la ventana con la piel umbralizada
        cv2.imshow('Ventana deteccion piel', piel_umbralizada)

    #Romper el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Liberamos la camara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()


