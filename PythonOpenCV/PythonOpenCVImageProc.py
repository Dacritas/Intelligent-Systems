#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
import cv2
from matplotlib import pyplot as plt

'''
#Lista las posibles conversiones de color.
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
'''


'''
#Algunas trasnformaciones del espacio de color.
img = cv2.imread('BumPumKapow.jpg',cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite('BumPumKapow_gray.png',gray_img)
cv2.imwrite('BumPumKapow_hsv.png',hsv_img)
'''

#Thresholding
img = cv2.imread('BumPumKapow_gray.png',0) #La imagen debe estar en escala de grises.
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()