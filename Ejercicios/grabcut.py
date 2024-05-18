import numpy as np
import cv2
from matplotlib import pyplot as plt
original = cv2.imread('..\Fotos\statue.jpg')
img = original.copy()
mask = np.zeros(img.shape[:2], np.uint8)		

#modelo de fondo y primer plano relleno de 0
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


#rectangulo inicial para los modelos de grabcut
rect = (150, 1, 421, 378) 

#ejecutar el algoritmo con lo definido anteriormente
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 120, cv2.GC_INIT_WITH_RECT) 


mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8') 
img = img*mask2[:,:,np.newaxis] 

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("grabcut")
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.xticks([])
plt.yticks([])
plt.show()
