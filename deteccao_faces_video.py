# Detecta faces em video

# importa bibliotecas  
import cv2
import numpy as np
import os

scale_factor = 1.2
min_neighbors = 3
min_size = (50, 50)

# carrega o algoritmo Cascade para detecao de face e atribui o modelo a variavel face_cascade
#face_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
face_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_eye.xml'))

video_cap = cv2.VideoCapture(0) # use 0,1,2..depanding on your webcam

while True:
    # Capture frame-by-frame
    ret, img = video_cap.read()

    ## converte em escala de cinza (grayscale) para processamento mais rapido
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rects = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                        minSize=min_size)
    # if at least 1 face detected
    if len(rects) >= 0:
        # Draw a rectangle around the faces
        for (x, y, w, h) in rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Detection on Video', img)
        #wait for 'c' to close the application
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    #tecla "esc" tem ascii código 27
    if cv2.waitKey(10) & 0xff == 27:
        video_cap.release()
        cv2.destroyAllWindows()