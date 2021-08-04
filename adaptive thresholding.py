import cv2
#adaptive threshold calculate value of threshold for small region of images so we get different
#       values for different regions of same image

img=cv2.imread('resources/sudoku.png')
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
# th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);


cv2.imshow("img",img)
cv2.imshow("th1",th1)
# cv2.imshow("th2",th2)
# cv2.imshow("th3",th3)



cv2.waitKey(0)
cv2.destroyAllWindows()