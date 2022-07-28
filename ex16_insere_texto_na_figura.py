# Cria texto em imagem
  
# importa bibliotecas
import cv2
import numpy as np

#Le figura
img = cv2.imread('.\imagens\dogs.jpg')
print(img.shape)

# fonte
fonte = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 35)
  
# escala da fonte
escala_fonte = 0.7

# cor azul em BGR
cor = (255, 0, 0)

# espessura da linha de 2 px
espessura = 5

# o metodo cv2.putText() insere texto na imagem
image_result = cv2.putText(img, 'OpenCV no IFMT', org, fonte, 
                   escala_fonte, cor, espessura, cv2.LINE_AA)
 
# plota a imagem na tela
cv2.imshow('Imagem com circulo', img) 

#tecla "esc" tem ascii código 27
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()   




