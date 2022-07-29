# Detecta faces em video

#importa biblioteca
import cv2

# captura video da camera
#video = cv2.VideoCapture(0)
video = cv2.VideoCapture('.\\videos\pessoas.mp4')


# enquanto o video estiver rodando repete o loop
while video.isOpened():
    ret, quadro = video.read()
    # se nao houver retorno em ret, indica fim do video
    if not ret:
        break
    # converte em escala de cinza (grayscale) para processamento mais rapido
    img = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    #classificador_face = cv2.CascadeClassifier(
    #    f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
    classificador_face = cv2.CascadeClassifier('.\\XML\\haarcascade_frontalface_default.xml')

    # faz a detecao das objetos (faces) e os insere na matriz definida pelo variavel objetos_detectados
    objetos_detectados = classificador_face.detectMultiScale(
        img, minSize=(100, 100)) # minSize indica o tamanho minimo are a ser detectada

    # plota um retangulo azul em cada face detectada, se houver
    if len(objetos_detectados) != 0:
        for (x, y, altura, largura) in objetos_detectados:
            cv2.rectangle(
                quadro, (x, y), ((x + altura), (y + largura)), (255, 0, 0), 5)

    # mostra o video com as faces detectadas
    cv2.imshow('Detecta face', quadro)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
