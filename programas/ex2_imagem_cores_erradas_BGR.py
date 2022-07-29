#Funcioando, mas como o própro OpenCV salva e le a figura, nao ocorre problem de RGB e BGR
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(".\imagens\\villages-in-switzerland.jpg")

#Plotando a imagem com o método  plt.imshow() 
#plt.imshow(img)
#RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.imshow(RGB_img)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

# display that image
plt.show()

