# Detecta olho em video

#importa biblioteca
import cv2

# captura video da camera
video = cv2.VideoCapture(0)

# enquanto o video estiver rodando repete o loop
while video.isOpened():
    ret, quadro = video.read()
    # se nao houver retorno em ret, indica fim do video
    if not ret:
        break
    # converte em escala de cinza (grayscale) para processamento mais rapido
    img = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    # carrega o algoritmo Cascade para detecao olho e o atribui a variavel classificador_face
    classificador_olho = cv2.CascadeClassifier(
        f"{cv2.data.haarcascades}haarcascade_eye.xml")

    # faz a detecao das objetos (olhos) e os insere na matriz definida pelo variavel objetos_detectados
    olhos_detectados = classificador_olho.detectMultiScale(
        img, minSize=(20, 20)) # minSize indica o tamanho minimo de area a ser detectada

    # plota um retangulo azul em cada oho detectado, se houver
    if len(olhos_detectados) != 0:
        for (x, y, altura, largura) in olhos_detectados:
            cv2.rectangle(
                quadro, (x, y), ((x + altura), (y + largura)), (255, 0, 0), 5)

    # mostra o video com as olhos detectados
    cv2.imshow('Detecta face', quadro)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()