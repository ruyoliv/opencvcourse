# Desloca uma imagem
   
# importa bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt  

# Cria a matriz de deslocamento (translacao).
# Se o desolccamento e de (x, y), entao a matriz seria
# M = [1 0 x]
#	 [0 1 y]
# Vamos deslocar aqui de (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

try:
    # leitura da imagem
    img = cv2.imread('.\imagens\dogs.jpg') 
  
    # dimensoes da imagem em termos de pixels.
    (linhas, colunas) = img.shape[:2]
      
    # a o metodo warpAffine realiza o desolocamento com base na matriz de deslocamento
    res = cv2.warpAffine(img, M, (colunas, linhas))

    #converte para RGB e plota numa unica imagem
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    RGB_img_rot = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    plt.subplot(2, 1, 1)
    plt.imshow(RGB_img)
    plt.subplot(2, 1, 2)
    plt.imshow(RGB_img_rot)

    # plota as duas imagens
    plt.show()
    # salva a imagem resultante no disco
    cv2.imwrite('.\output_images\img_deslocada.jpg', res)
except IOError:
    print ('Erro na leitura do arquivo !!!')
