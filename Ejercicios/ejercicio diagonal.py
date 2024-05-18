import cv2

#Leemos la imagen.
image=cv2.imread('..\Fotos\planet_glow.jpg')

#Leemos la imagen en blanco y negro y la guardamos para acceder a ella.
image2=cv2.imread('..\Fotos\planet_glow.jpg',0)
cv2.imwrite('..\Fotos\planetBW.jpg',image2)

#Abrimos la imagen en blanco y negro para dibujar sobre ella.
image3= cv2.imread('..\Fotos\planetBW.jpg',1)

#Cogemos las características.
forma=image.shape

print(forma)
#Sacamos la relación de aspecto para dibujar bien la diagonal.
relacionAspecto=forma[1]/forma[0]

#Pintamos la diagonal.
for i in range(0,forma[0]):
    pixelAlto=int(i*relacionAspecto)
    image3[i,pixelAlto]=image[i,pixelAlto]
    
    #Pintamos uno más para que se vea mejor.
    image3[i,pixelAlto+1]=image[i,pixelAlto+1]
    
#Vemos la nueva imagen.
cv2.imshow('planetas_diagonal',image3)
cv2.waitKey(0)



