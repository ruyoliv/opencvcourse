# Detecta carro 

# importa as biblioteca
import cv2

# # carrega video de arquivo
cap = cv2.VideoCapture('.\\videos\\cars2.mp4')

# arquivo XML com descrição de caracteristicas do objeto que se quer detectar
classificador_carro = cv2.CascadeClassifier('.\XML\\cars.xml')

# repete ate o final do video
while True:
    # le quadros do video
    ret, quadro = cap.read()
	
    # converte em escala de cinza (grayscale) para processamento mais rapido
    img_cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)
	
    # Detecta carros de diferentes tamanhos na imagem cinza
    carros = classificador_carro.detectMultiScale(img_cinza, 1.1, 1)
	
    # plota um retangulo azul em cada carro detectado, se houver
    for (x,y,w,h) in carros:
        cv2.rectangle(quadro,(x,y),(x+w,y+h),(0,0,255),2)
    
    # mostra video com carros detetados
    cv2.imshow('Deteccao de carros', quadro)
    
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
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
