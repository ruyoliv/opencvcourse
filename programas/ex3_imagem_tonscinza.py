#Plotando figura em tom de cinza
import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r'.\imagens\villages-in-switzerland.jpg'  
img=cv2.imread(path,0) # 0 corresponde ao modeo grayscale

# Plota a imagem na tela
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
