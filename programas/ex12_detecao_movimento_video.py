# Detecta movimento em video - Subtracao de plano de fundo
  
# importa bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt 

#le video
cap = cv2.VideoCapture('.\\videos\\frog.mp4')
#gera o modelo de subtração
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    # ret recebe true se a leitura estiver correta, ou false caso contrario 
    # frame recebe um quadro do video (matriz), baseado na taxa de quadros por segundos sendo usada
    ret, frame = cap.read()
    
    #aplica o modelo de subtração na sequencia de quadros do video
    #fmask é o resultado denominado "mascara de primeiro plano"
    fgmask = fgbg.apply(frame)

    # plota os dois quadro sucessivos (duas imagens)
    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame',frame )

    k = cv2.waitKey(30) & 0xff # espera 30 milisegundos
    if k == 27:  #esc tem ascii código 27
        break
	
cap.release()
cv2.destroyAllWindows()


