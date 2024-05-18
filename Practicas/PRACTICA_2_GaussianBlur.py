import cv2
import time

#Capturamos el video
captura = cv2.VideoCapture(0)

while True:
    #Capturamos fotograma del video
    ret, fotograma = captura.read()

    #Rompe el bucle si no puede capturar el fotograma
    if not ret:
        break

    #Aplicamos filtro de paso bajo (GaussianBlur) 
    fotograma_suavizado = cv2.GaussianBlur(fotograma, (7, 7), 10)
    #Creamos una mascara con los valores BGR de la piel, usando como ejemplo los valores obtenidos de la foto de Gorka
    mascara = cv2.inRange(fotograma_suavizado, (20, 52, 90), (150, 210, 220))
    #Aplicamos la mascara al fotograma
    resultado = cv2.bitwise_and(fotograma, fotograma, mask=mascara)
    #Mostramos el resultado obtenido.
    cv2.imshow('Ventana', resultado)

    #Capturamos la imagen y cierre del programa
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        timestamp = int(time.time())  
        fichero = f'{timestamp}.jpg' 
        cv2.imwrite(fichero, resultado)
    elif key == ord('q'):
        break

#Liberar la camara
captura.release()
cv2.destroyAllWindows()




