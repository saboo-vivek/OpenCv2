## using image pyramid the resolution og image decreases by 1/4 at each level
## pyr down decreases the resolution
## pyr up increases the resolution
import  cv2
import  numpy as np

img=cv2.imread('resources/lena.jpg')
#--------------------------------GAUSSIAN MAETHOD --------------------------------------------------------
# lr1=cv2.pyrDown(img)
# lr2=cv2.pyrDown(lr1)
# lr3=cv2.pyrDown(lr2)
# hr1=cv2.pyrUp(lr2)
#
# cv2.imshow('Original image',img)
# cv2.imshow('PyrDown 1',lr1)
# cv2.imshow('PyrDown 2',lr2)
# cv2.imshow('PyrDown 3',lr3)
# cv2.imshow('PyrUp 1',hr1)

# # --------- or using for loop
# layer=img.copy()
# gp=[layer]

# for i in range(6):   ### we have to gave range ==6 for showing 5 images because range goes no -1
#     layer=cv2.pyrDown(layer)
#     gp.append(layer)
#     cv2.imshow(str(i),layer)
#
# cv2.imshow("original",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


##----------------------USING LAPLACIAN METHOD--------------------
layer=img.copy()
cv2.imshow("layer agter lapla",layer)
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)

for i in range(5,0,-1):   ### we have to gave range ==6 for showing 5 images because range goes no -1
    gau_extended=cv2.pyrUp(gp[i])
    lapla=cv2.subtract(gp[i-1],gau_extended)
    cv2.imshow(str(i),lapla)

cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()