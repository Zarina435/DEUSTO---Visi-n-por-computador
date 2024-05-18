import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage

#------------------------------------------------------------------------------
#Espectro de magnitud.
#Cargamos la foto.
img_color = cv2.imread('..\Fotos\planet_glow.jpg')
#Pasamos a escalas de grises.
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#Creamos el vector de la imagen.
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
#Aplicamos la transformada de Fourier.
dft_shift = np.fft.fftshift(dft)
#Obtenemos el espectro de magnitud.
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

#Mostramos las dos imágenes.
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#------------------------------------------------------------------------------
#FILTROS DE PASO BAJO. (para eliminar ruido)
#Obtenemos las dimensiones de la imagen.
rows, cols = img.shape
crow,ccol = rows//2 , cols//2

#Creamos el vector de la máscara.
mask = np.zeros((rows,cols,2),np.uint8)
#Cambiamos los valores.
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

#A la transformada de Fourier le aplicamos la máscara.
fshift = dft_shift*mask
#Obtenemos la transformada.
f_ishift = np.fft.ifftshift(fshift)
#Revertimos la transformada
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

#Mostramos las dos imágenes.
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])
plt.show()

#------------------------------------------------------------------------------
#FILTROS DE PASO ALTO. (para marcar más los bordes)
#Definimos el kernel.
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

#Aplicamos los kernels.
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

#Aplicamos ruido gaussiano.
blurred = cv2.GaussianBlur(img, (17,17), 0)
#A la imagen original, le quitamos el desenfoque para quedarnos con la mayor diferencia.
g_hpf = img - blurred

#Mostramos las nuevas imágenes.
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("blurred", blurred)
cv2.imshow("g_hpf", g_hpf)

cv2.waitKey()
cv2.destroyAllWindows()
