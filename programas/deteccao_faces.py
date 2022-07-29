# Detecta faces

# importa bibliotecas  
import cv2
import numpy as np
import os

# carrega o algoritmo Cascade para detecao de face e atribui o modelo a variavel face_cascade
face_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))

# le figura
img = cv2.imread('.\\imagens\\faces.png')
print(img.shape)

# converte em escala de cinza (grayscale)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecta as facess
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print(faces)

# insere um retangulo ao redor de cada face detectada
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Plota resultado na tela
cv2.imshow('imagem', img)

#tecla "esc" tem ascii código 27
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows() 