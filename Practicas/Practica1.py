import cv2
import numpy as np

inicio=True
cont=0
    
#Definimos el evento de ratón cuando se clicka.
def onMouse(event,x,y,flags,param):
    #Cuando se haga click, se entrará en la función de gestión.
    if event == cv2.EVENT_LBUTTONUP:
         gestion(x,y)

#Función de gestión.
def gestion(x,y):
    
    #Definimos las variables.
    global inicio
    global punto_inicial
    global punto_intermedio1
    global punto_intermedio2
    global punto_final
    global cont
    
    #Si es el primer punto, actualizamos los puntos correspondientes.
    if inicio:
        punto_inicial=(x,y)
        punto_intermedio1=(x,y)
    #Si es el segundo punto, actualizamos los puntos correspondientes y dibujamos.
    elif cont==1:
        punto_intermedio1=punto_inicial
        punto_intermedio2=(x,y)
        cv2.line(image,punto_intermedio1,punto_intermedio2,(255,0,0),10) 
    #Si es el tercer o cuarto punto, actualizamos los puntos correspondientes y dibujamos.
    elif cont<4:
        punto_intermedio1=punto_intermedio2
        punto_intermedio2=(x,y)
        cv2.line(image,punto_intermedio1,punto_intermedio2,(255,0,0),10) 
    #Si es el último punto, lo actualizamos y dibujamos.
    elif cont==4:
        punto_final=(x,y)
        cv2.line(image,punto_intermedio2,punto_final,(255,0,0),10) 
        cv2.line(image,punto_final,punto_inicial,(255,0,0),10) 
    #Si se clicka más veces no se tendrá en cuenta.
    else:
        print('No se admiten más puntos.')
    
    #Actualizamos variables.
    inicio=False
    cont+=1
    
    #Mostramos la imagen con las líneas.
    cv2.imshow('Imagen',image)
         
 
#Abrimos la foto.
image=cv2.imread('..\Fotos\planet_glow.jpg',1)

#Mostramos la imagen.
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen',onMouse)
cv2.imshow('Imagen',image)

#Cerramos la ventana.
cv2.waitKey()
cv2.destroyAllWindows()