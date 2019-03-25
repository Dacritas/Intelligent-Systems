#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html#histograms-getting-started
import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
#Histograma simple
img = cv2.imread('Simpson.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()
'''

#Histograma de Color
img = cv2.imread('Simpson.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()