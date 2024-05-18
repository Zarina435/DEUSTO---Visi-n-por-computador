import cv2
import numpy as np

#Capturamos el video
cap = cv2.VideoCapture(0)

while True:
    #Capturamos cada frame del video
    ret, frame = cap.read()
    
    #Creamos un rectangulo para determinal el ROI (x, y, ancho, alto)
    rect = (50, 50, 400, 400)
    #Creamos una mascara de inicio
    mascara = np.zeros(frame.shape[:2], np.uint8)
    
    #Creamos las matrices que utilizara grabcut
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    #Aplicamos grabcut al frame video utilizando el rectangulo
    cv2.grabCut(frame, mascara, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
    
    #Creamos una mascara binaria, los pix etiquetados como probable piel (2), seguro son piel (3)
    mascara2 = np.where((mascara == 2) | (mascara == 0), 0, 1).astype('uint8')
    
    #Aplicamos la mascara al frame
    piel_detectectada = frame * mascara2[:, :, np.newaxis]
    # Mostrar el cuadro con la máscara de piel
    cv2.imshow('Ventana deteccion piel', piel_detectectada)

    #Romper el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Liberamos la camara y cerramoslas ven tanas
cap.release()
cv2.destroyAllWindows()



