# Preenche centro da imagem com uma cor definida aqui

#importa biblioteca
import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread(".\imagens\\dogs.jpg", cv2.IMREAD_COLOR)

#obtem altura e largura da imagem - em PIXELs
(altura, largura ) = img.shape[:2]

metade_alt = int(altura/2)
metade_larg = int(largura/2)
# valores para tamanho do preenchimento da imagem, de altura e largura
tam_preench_a = 10
tam_preench_l = 100

#preenche centro da imagem com cor azul - aqui no Opencv o padrao e BGR
img[metade_alt - tam_preench_a : metade_alt + tam_preench_a, 
    metade_larg - tam_preench_l : metade_larg + tam_preench_l] = [255,0,0]

# Cria janela GUI para plotar imagem na tela
cv2.imshow("dogs", img)

#espera qualquer tecla ser pressionada para continuar
cv2.waitKey(0)

# remove janela GUI criada da tela e memória
cv2.destroyAllWindows()










''''
#width=259
#height = 194
'
#preenche uma faixa vertical do lado direito da imagem de cor verde
img[:,largura - 50 : largura] = [255,0,0]

#copia parte da imagem para outra posicao
img[0:70,0:70] = img[metade_alt-35:metade_alt+35, metade_larg-35:metade_larg+35]

'''


