# Filtra cor na imagem/video
  
# importa bibliotecas
import cv2
import numpy as np

#captura video da Webcam
cap = cv2.VideoCapture(0)

while(1):
    # ret recebe true se a leitura estiver correta, ou false caso contrario 
    # frame recebe um quadro do video (matriz), baseado na taxa de quadros por segundos sendo usada
    _ , frame = cap.read()

    # converte padrao de cor BGR para HSV - e mais adequado para essas aplicacoes
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # limites da cor verde no padrao HSV - hsl(hue, saturation, lightness)
    # intensidade (0 a 360 graus), saturacao (0 a 100%), brilho (0 a 100%)
    #verde_inf = np.array([25, 20, 20])  
    #verde_sup = np.array([100, 255, 255])
    #relativamente bom
    verde_inf = np.array([25, 50, 50]) 
    verde_sup = np.array([100, 255, 255])
    #melhor ainda
    verde_inf = np.array([25, 50, 70]) 
    verde_sup = np.array([100, 255, 255])

    verde_inf = np.array([25, 70, 70]) 
    verde_sup = np.array([100, 255, 255])

    # preparo da mascara para sobreposicao
    masc = cv2.inRange(hsv, verde_inf, verde_sup)

    # a regiao preta na mascara tem valor 0, de modo que quando multiplicada
    #  logicamente (via E logico) com a imagem original remove as regioes nao verdes
    result = cv2.bitwise_and(frame, frame, mask = masc)

   # plota: imagem original, mascara e imagem resultante
    cv2.imshow('frame', frame)
    cv2.imshow('mask', masc)
    cv2.imshow('result', result)

    k = cv2.waitKey(1) & 0xff 
    if k == 27:  #esc tem ascii código 27
        break
# libera o espaco em memoria usado pelo video e pela janela de impressao na tela
cap.release()
cv2.destroyAllWindows()
