# Rotaciona uma imagem
   
# importa bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt  

path = r'.\imagens\dogs.jpg' 
 
try:
    # leitura da imagem
    img = cv2.imread(path)
  
    # Shape of image in terms of pixels.
    (linhas, colunas) = img.shape[:2]
      
    # getRotationMatrix2D cria a matriz necessária à transformação
    # parametros para centralzar rotacionar 45 graus sem mudanca de tamanho (fator de escala igual a 1)
    M = cv2.getRotationMatrix2D((colunas / 2, linhas / 2), 45, 1)
    #res = cv2.warpAffine(img, M, (colunas, linhas))
    print(linhas, colunas, linhas/2,colunas/2)
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
    cv2.imwrite('.\output_images\img_rotacionada.jpg', res)
except IOError:
    print ('Erro na leitura do arquivo !!!')



