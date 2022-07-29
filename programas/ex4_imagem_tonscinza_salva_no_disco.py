#Plotando figura em tom de cinza e salvando-a no disco
import cv2
import numpy as np
import matplotlib.pyplot as plt
path_in = r'.\imagens\villages-in-switzerland.jpg'  
img=cv2.imread(path_in,0) # 0 corresponde ao modeo grayscale

# Plota a imagem na tela
cv2.imshow('imagem', img)
# Salva no disco
path_out = r'.\output_images\Suica_tonscinza.jpg'
nome_img_salva = "Suica_tonscinza.jpg"
cv2.imwrite(path_out, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
