import cv2
import numpy as np

def click_event(event,x,y,flags,param):

    # #left click event to draw line bet pts
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img,(x,y),3,(0,0,255),-1,) ## thickness -1 fills the circle
    #     pts.append((x,y))
    #     if len(pts)>=2:
    #         cv2.line(img,pts[-1],pts[-2],(255,0,0),5)
    #     cv2.imshow('image',img)
    #

## to show the color at another window at x,y
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green= img[x,y, 1]
        red= img[x,y, 2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        colorimage=np.zeros((512,512,3),np.uint8)
        colorimage[:]=[blue,green,red]   ## [:] select all chanels and all matrix pts/pixels
        cv2.imshow('color window',colorimage)




img=cv2.imread("resources/lena.png")
# img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
pts=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()