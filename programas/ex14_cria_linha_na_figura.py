# Cria linha em imagem
  
# importa bibliotecas
import cv2
import numpy as np

#Le figura
img = cv2.imread('.\imagens\dogs.jpg')
print(img.shape)

# coordenada do ponto inicial, aqui (0, 0), canto superior esq. da imagem
ponto_inicial = (0, 0)

#cCoordenada do ponto final, aqui (258, 194), canto inferior dir. da imagem
ponto_final = (258, 194)

# Cor verde em BGR
cor = (0, 255, 0)

# espessura da linha de 9 px
espessura = 9

# Usando o metodo cv2.line() para criar um linha diagonal com espessura de 9 px
#cv2.line(img, ponto_inicial, ponto_final, cor, espessura)

cv2.arrowedLine(img, ponto_inicial, ponto_final, cor, espessura)
 
# plota a imagem na tela
cv2.imshow('Imagem com linha', img) 

#tecla "esc" tem ascii código 27
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()     

