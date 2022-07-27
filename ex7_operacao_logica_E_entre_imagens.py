# Realiza a operacao lógica E entre duas imagens
   
# importa bibliotecas
import cv2
import numpy as np
   
# leitura das imagens 
path1 = r'.\imagens\quadrados_preto_branco.png' 
path2 = r'.\imagens\retangulo_preto_com_bola_branca_no_meio.png' 
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# realiza o E logico entre as duas imagens
dest_and = cv2.bitwise_and(img2, img1, mask = None)
 
# plota as duas mensagens originais e a imagem resultante
cv2.imshow('Imagem 1', img1)
cv2.imshow('Imagem 2', img2)
cv2.imshow('Imagem resultante', dest_and)
 
# libera espacoes em memoria utilizado 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()