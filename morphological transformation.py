import cv2
import numpy as np
from matplotlib import  pyplot as plt

img=cv2.imread('resources/smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((5,5),np.uint8)

dilation=cv2.dilate(mask,kernal,iterations=2)
erosion=cv2.erode(mask,kernal,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)   ## erosion then dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)  ## dilation first and then erosion

titles = ['original image','mask','dilation','eroded','opening','closing']
images = [img,mask,dilation,erosion,opening,closing]

for i in range(6):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  ## to remove x/y axis marking

plt.show()