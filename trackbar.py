import cv2
import numpy as np

def empty(a):
    pass

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("TrackBars")

cv2.createTrackbar("blue","TrackBars",0,255,empty)
cv2.createTrackbar("green","TrackBars",0,255,empty)
cv2.createTrackbar("red","TrackBars",0,255,empty)
switch='0 : OFF\n 1 : ON'
cv2.createTrackbar(switch,"TrackBars",0,1,empty)

while True:
    cv2.imshow("TrackBars", img)
    b = cv2.getTrackbarPos("blue", "TrackBars")
    g = cv2.getTrackbarPos("green","TrackBars")
    r= cv2.getTrackbarPos("red", "TrackBars")
    s= cv2.getTrackbarPos(switch, "TrackBars")

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]


    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()