#Funcioando, mas como o própro OpenCV salva e le a figura, nao ocorre problem de RGB e BGR
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(".\imagens\\villages-in-switzerland.jpg")

#Plotando a imagem com o método  plt.imshow() 
'''
dir = "C:\\Users\\Ruy\\Documents\\OpenCV_Programas\\imagens\\"
cv2.imwrite(dir+'tmp.jpg', img)
with Image.open(dir+'tmp.jpg') as img:
    img.show()'
'''
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.imshow(RGB_img)

 
# display that image
plt.show()

