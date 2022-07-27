# Altera tamanho de imagens
   
# importa bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt   
# leitura das imagens 
path = r'.\imagens\frutas.png' 
img = cv2.imread(path) 
 
metade = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
maior = cv2.resize(img, (1050, 1610))
 
stretch_near = cv2.resize(img, (780, 540),
               interpolation = cv2.INTER_NEAREST)
 
 
Titles =["Original", "Metade", "Maior", "Interpolação"]
images =[img, metade, maior, stretch_near]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()
