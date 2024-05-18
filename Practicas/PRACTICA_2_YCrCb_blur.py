import cv2
import time
import numpy as np

# Capturamos el video
captura = cv2.VideoCapture(0)

while True:
    #Capturamos fotograma del video
    ret, frame = captura.read()
    
    # Normalizamos la iluminacion aplicando una correccion gamma
    gamma = 1.5
    frameNormalizado = np.clip(np.power(frame / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)
    
    #Aplicamos un filtro de paso bajo.
    dst = cv2.GaussianBlur(frameNormalizado, (7,7), 10)
    
    #Convertimos el frame normalizado a YCrCb
    YCrCb = cv2.cvtColor(dst, cv2.COLOR_BGR2YCrCb)
    
    #Rango del color de la piel en formato YCrCb
    tonoBajo = np.array([0, 133, 77], dtype=np.uint8)
    tonoAlto = np.array([255, 193, 147], dtype=np.uint8)
    
    #Creamos una mascara con los valores YCrCb de la piel
    mascara = cv2.inRange(YCrCb, tonoBajo, tonoAlto)

    #Aplicamos la mascara al fotograma
    soloPiel = cv2.bitwise_and(frameNormalizado, frameNormalizado, mask=mascara)
    
    #Mostramos el resultado obtenido
    cv2.imshow('Ventana', soloPiel)

    #Capturamos la imagen y cierre del programa
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        timestamp = int(time.time())
        file_name = f'{timestamp}.jpg'
        cv2.imwrite(file_name, soloPiel)
    elif key == ord('q'):
        break

# Liberar la camara
captura.release()
cv2.destroyAllWindows()



