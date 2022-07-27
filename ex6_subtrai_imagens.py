# Realiza a subtracao de duas imagens
   
# importa bibliotecas
import cv2
import numpy as np
   
# leitura das imagens 
path1 = r'.\imagens\800_600_img1.jpg' 
path2 = r'.\imagens\800_600_img2.jpg' 

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# soma as duas imagens
sub = cv2.subtract(img1,img2)
 
# plota as duas mensagens originais e a imagem resultante
cv2.imshow('Imagem 1', img1)
cv2.imshow('Imagem 2', img2)
cv2.imshow('Imagem resultante', sub)
 
# libera espacoes em memoria utilizado 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()