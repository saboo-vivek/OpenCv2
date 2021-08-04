import cv2
import numpy as np

def click_event(event,x,y,flags,param):

    #left click event to display (x,y) at (x,y) position
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,244,255),2)
        cv2.imshow('image',img)

    #right click event to display bgr value at (x,y) position
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green= img[y, x, 1]
        red= img[y, x, 2]
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)
        cv2.imshow('image', img)

img=cv2.imread('resources/ferari.png')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)