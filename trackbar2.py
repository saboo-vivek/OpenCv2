import cv2
# import numpy as np

def empty(a):
    pass



cv2.namedWindow("TrackBars")
cv2.createTrackbar("green","TrackBars",15,255,empty)

switch='color/gray'
cv2.createTrackbar(switch,"TrackBars",0,1,empty)

while True:
    img = cv2.imread("resources/ww.png")
    pos = cv2.getTrackbarPos("green","TrackBars")
    s = cv2.getTrackbarPos(switch, "TrackBars")
    cv2.putText(img,str(pos),(50,150),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(0,255,0),2)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("TrackBars",img )


cv2.destroyAllWindows()