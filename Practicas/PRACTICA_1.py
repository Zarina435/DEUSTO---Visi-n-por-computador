import cv2  #Biblioteca OpenCV para el procesamiento de imágenes
import numpy as np  #Biblioteca NumPy para operaciones matemáticas

#Cargamos la imagen
image = cv2.imread('../Fotos/planet_glow.jpg')

#Inicializamos las variables para controlar el poligono
lados = 4  # Número de lados que tendrá el polígono
poligono_puntos = []  # Lista para almacenar las coordenadas del polígono
poligono_estado = False  # Variable para controlar si el polígono está cerrado o no

#Función para dibujar líneas entre los puntos al hacer clic con el ratón
def draw_lines(event, x, y, flags, param):
    
    global poligono_puntos, lados, poligono_estado  #Definimos las variables de manera global
    if event == cv2.EVENT_LBUTTONDOWN and len(poligono_puntos) < lados:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)  #Dibujamos un círculo de radio 2 al hacer clic
        #Al hacer clic izquierdo y si no se han seleccionado todos los puntos del polígono
        poligono_puntos.append((x, y))  #Agregamos las coordenadas al array de puntos del poligono
        if len(poligono_puntos) > 1:
            cv2.line(image, poligono_puntos[-2], poligono_puntos[-1], (0, 0, 255), 1)  # Dibujamos una línea entre los dos últimos puntos clikados
            
            cv2.imshow('Imagen recortada', image)  # Mostramos la imagen con las lineas que vamos pintando
        if len(poligono_puntos) == lados:
            cv2.line(image, poligono_puntos[-1], poligono_puntos[0], (0, 0, 255), 1)  # Cerramos el polígono dibujando una línea entre el primer y último punto
            poligono_estado = True  #Marcamos el estado del polígono a cerrado
            cv2.imshow('Imagen recortada', image)  #Mostramos la imagen con el polígono ya cerrado

cv2.imshow('Imagen recortada', image)  #Mostramos la imagen cargada
cv2.setMouseCallback('Imagen recortada', draw_lines)  #Asociamos la función draw_lines a la ventana para gestionar los eventos del ratón
while True:
    #Dibujar textos en la imagen
    cv2.putText(image, 'r: resetear', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)  #Muestra 'r: resetear' en la posición (10, 30)
    cv2.putText(image, 's: guardar poligono', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)  #Muestra 's: guardar poligono' en la posición (10, 60)
    cv2.putText(image, 'esc: salir', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)  #Muestra 'esc: salir' en la posición (10, 90)
    cv2.imshow('Imagen recortada', image)  #Muestra la imagen con los textos añadidos
    
    key = cv2.waitKey(1) & 0xFF  #Espera por la entrada del teclado y almacena el valor de la tecla presionada en la variable 'key'
    #Presionar 'r' para reiniciar el poligono
    if key == ord('r'):
        poligono_puntos = []  # Resetea la lista de puntos del polígono
        poligono_estado = False  #Marca el polígono como no cerrado
        image = cv2.imread('../Fotos/planet_glow.jpg')  #Recarga la imagen a su estado inicial
    #Presionar 's' para guardar el polígono
    elif key == ord('s'):
        if poligono_estado:
            points = np.array(poligono_puntos, np.int32)  #Convierte la lista de puntos del poligono en un array
            cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=1)  #Dibujamos el polígono en la imagen
            x, y, w, h = cv2.boundingRect(points)  #Generamos un rectángulo delimitador del polígono
            cropped_image = image[y:y+h, x:x+w]  #Recortamos la imagen según el polígono generado
            cv2.imwrite('imagen_recortada.jpg', cropped_image)  #Guardamos la parte del polígono como una nueva imagen
            cv2.putText(image, 'Recorte guardado', (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)  #Muestra texto de recorte guardado en la esquina inferior izquierda
    # Presionar 'esc' para salir del programa
    elif key == 27:
        break  #Salimos del bucle y termina el programa

cv2.destroyAllWindows()  #Cerramos todas las ventanas abiertas