import cv2
import numpy as np

color_explore = np.zeros((100,400, 3), np.uint8)
color_selected = np.zeros((100,400, 3), np.uint8)

# boardimg = np.zeros((775,1024,3),np.uint8)
# boardimg[:]= (255,255,255)

mycolorvalues=[]

myPoints =  []  ## [x , y , colorId ]
################################################################################################
# Mouse Callback function
def show_color(event, x, y, flags, param):
    B = img[y, x][0]
    G = img[y, x][1]
    R = img[y, x][2]

    color_explore[:] = (B,G,R)

    if event == cv2.EVENT_LBUTTONDOWN:
        mycolorvalues = [B, G, R]
        color_selected[:] = mycolorvalues


#############################################################################################
# image window for sample image
cv2.namedWindow('COLOR PICKER')

# read sample image
img = cv2.imread('colorpick.png')
img=cv2.resize(img,(400,400))

# mouse call back function declaration
cv2.setMouseCallback('COLOR PICKER', show_color)
#################################################################################################

# while loop to live update
while (1):

    cv2.imshow('COLOR PICKER', img)
    cv2.imshow('color_explore', color_explore)
    cv2.imshow('color_selected', color_selected)
    # cv2.imshow('Board',boardimg)

    k = cv2.waitKey(1) & 0xFF
    if k ==ord('q') or k ==ord('Q') :
        break

cv2.destroyAllWindows()

