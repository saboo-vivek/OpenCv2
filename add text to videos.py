import cv2
import datetime
import  numpy as np

cap=cv2.VideoCapture(0)

##the camera will take only the available nearest resolution
cap.set(3,1280) ## frame width
cap.set(4,720) ## frame height

while True:
    success,frame=cap.read()

    frame=cv2.flip(frame,1)
    # 0 for vertically
    # 1 for horizontally
    # -1 for both hori and verti

    text='Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
    datet=str(datetime.datetime.now())
    frame = cv2.putText(frame,datet, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 233, 233), 2, cv2.LINE_AA)
    # frame = cv2.putText(frame,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,233,233),2,cv2.LINE_AA)
    cv2.imshow('video capture',frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()