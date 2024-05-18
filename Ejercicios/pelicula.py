import cv2

#Definimos los eventos y ponemos su valor a false.
left_clicked = False
right_clicked = False

#Definimos las acciones de los eventos y cuándo se van a capturar.
def onMouse(event, x, y, flags, param):
    #Primero las variables globales.
    global left_clicked
    global right_clicked
    
    #Click izquiero para capturar fotograma.
    if event == cv2.EVENT_LBUTTONUP:
        #Si se pulsa, lo ponemos a true.
        left_clicked = True
        print('Boton izquierdo pulsado')
    #Click derecho para cerrar ventana y parar.
    elif event == cv2.EVENT_RBUTTONUP:
        #Si se pulsa, lo ponemos a true.
        right_clicked = True
        print('Boton derecho pulsado')    

#Definimos la cantidad de fps.
fps = 30
#Capturamos con la cámara externa.
cameraCapture = cv2.VideoCapture(0)
#Definimos el tamaño del vídeo.
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#Definimos el formato del vídeo.
videoWriter = cv2.VideoWriter('Pelicula2.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps, size)

#Nombramos la ventana que va a abrirse.
cv2.namedWindow('MyWindow')
#Definimos los eventos en la ventana.
cv2.setMouseCallback('MyWindow', onMouse)
print('Showing camera feed. Click window or press any key to stop.')

#Capturamos primer fotograma.
success, frame = cameraCapture.read()

#Bucle paa capturar fotogramas.
while success and cv2.waitKey(1) == -1 and not right_clicked:
    #Si se pulsa el botón izquierdo, guardamos el fotograma.
    if left_clicked == True:
        #El fotograma se guarda 15 veces.
        for i in range(1,int(fps/2)):
            #Guardamos el fotograma.
            videoWriter.write(frame)
    #Volvemos a poner la variable a false para poder seguir comparado.
    left_clicked = False

    #Mostramos la ventana con el frame.
    cv2.imshow('MyWindow', frame)
    #Capturamos el siguiente frame.
    success, frame = cameraCapture.read()

#Cerramos la ventana al terminar.
cv2.destroyWindow('MyWindow')
#Liberamos la cámara al terminar.
cameraCapture.release()