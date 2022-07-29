# captura o video da webcam e coloca quatro imagens menores rotacionadas
# numa unica janela 

# importa bibliotecas
import numpy as np
import cv2

# le da webcam
cap = cv2.VideoCapture(0)

#muda a resolucao (size) das imagens
def muda_tam(larg,altura,frame):
    dim = (larg,altura)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

while True:
    # captura video
    ret, frame = cap.read()
 
    # muda tamanho da imagem
    frame = muda_tam(900,900,frame)
    width = frame.shape[0]
    height = frame.shape[1]

    # cria matriz de imagem grande e cria imagem menor, da grande
    img = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
   
    #posiciona imagens menores (giradas) em um unica imagem
    img[:width//2, :height//2] = smaller_frame
    img[:width//2, height//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)
    img[width//2:, height//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)	
    img[width//2:, :height//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
 
    cv2.imshow('frame', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()






















'''
#Funcionando para detectar faces

import cv2

window_name = "Detected Objects in webcam"
video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade_classifier = cv2.CascadeClassifier(
        f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
    detected_objects = cascade_classifier.detectMultiScale(
        image, minSize=(20, 20))

    if len(detected_objects) != 0:
        for (x, y, height, width) in detected_objects:
            cv2.rectangle(
                frame, (x, y), ((x + height), (y + width)), (0, 255, 0), 5)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
'''
