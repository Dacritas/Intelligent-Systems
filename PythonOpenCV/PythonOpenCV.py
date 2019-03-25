import numpy as np
import cv2


'''
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
#Cargar y mostrar una imagen. 
#Para cargarla en Escala de Grises utilice: cv2.IMREAD_GRAYSCALE.

img = cv2.imread('BumPumKapow.jpg',cv2.IMREAD_COLOR)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
#Crear una imagen, dibujar en ella y guardar el dibujo.
img = np.zeros((512,512,3), np.uint8) #Crea una imagen vacia
img = cv2.line(img,(0,0),(511,511),(255,0,0),5) #Dibuja una linea
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #Dibuja un rectangulo
img = cv2.circle(img,(447,63), 63, (0,0,255), -1) #Dibuja un circulo
#Dibuja un poligono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
#Pone texto sobre la imagen
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
#Muestra la imagen.
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Guarda la imagen
cv2.imwrite('my_picture.png',img)


'''
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops
img = cv2.imread('BumPumKapow.jpg',cv2.IMREAD_COLOR)
px = img[100,100] #obtiene el pixel (100,100)
print(px)
blue = img[100,100,0] #obtiene el componente blue. green=1, red=2.
print(blue)
img[100,100] = [255,255,255] #Modifica el pixel (100,100)
print(img[100,100])
print(img.shape) #imprime resolucion de la imagen.
print(img.size)#imprime tamaño de la imagen.
print(img.dtype) #imprime tipo de imagen.

b,g,r = cv2.split(img) #obtiene las matrices b, g, r
img = cv2.merge((b,g,r)) #recombina las matrices

#Extra la imagen del perro y la gurarda en otro archivo.
dog = img[10:70,127:206]
cv2.imwrite('dog.png',dog)
'''

'''
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#image-arithmetics
img1 = cv2.imread('BumPumKapow.jpg')
img2 = cv2.imread('Simpson.jpg')

dst = cv2.addWeighted(img1,0.6,img2,0.4,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
