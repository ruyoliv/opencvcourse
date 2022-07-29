# Cria circulo em imagem
  
# importa bibliotecas
import cv2
import numpy as np

#Le figura
img = cv2.imread('.\imagens\dogs.jpg')
print(img.shape)

# coordenada do centro do círculo
coordinadas_centro = (130, 150)

# raio do círculo
raio = 20

# cor vermelha em BGR
cor = (0, 0, 255)

# espessura da linha de 2 px
espessura = 5

# o metodo cv2.circle() cria um círculo com linha borda azul de espessura 5 px
image2 = cv2.circle(img, coordinadas_centro, raio, cor, espessura)
 
# plota a imagem na tela
cv2.imshow('Imagem com circulo', img) 

#tecla "esc" tem ascii código 27
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()   
