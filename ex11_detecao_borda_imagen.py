# Detecta bordas numa imagem
   
# importa bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt  

try:
    # leitura da imagem
    img = cv2.imread('.\imagens\dogs.jpg') 
    img = cv2.imread('.\imagens\cow1.jpg')
  
    # Canny edge detection.
    #t_lower = 50  # limite inferior de sensibilidade
    #t_upper = 150  # limite superior de sensibilidade
    img_bordas = cv2.Canny(img, 100, 200)
  
    #converte para RGB e plota numa unica imagem
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    RGB_img_rot = cv2.cvtColor(img_bordas, cv2.COLOR_BGR2RGB)
    plt.subplot(2, 1, 1)
    plt.imshow(RGB_img)
    plt.subplot(2, 1, 2)
    plt.imshow(RGB_img_rot)

    # plota as duas imagens
    plt.show()
    # salva a imagem resultante no disco
    cv2.imwrite('.\output_images\img_bordas.jpg', res)
except IOError:
    print ('Erro na leitura do arquivo !!!')

