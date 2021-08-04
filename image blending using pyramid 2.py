import cv2
import  numpy as np

apple=cv2.imread('resources/apple.jpg')
orange=cv2.imread('resources/orange.jpg')
print(apple.shape)
print(orange.shape)

## using normal method
apple_orange=np.hstack((apple[:, :256],orange[:, 256:]))

#------------------------using pryamid

#generate Guassian pyramid for apple
apple_copy=apple.copy()
gp_apple=[apple_copy]

for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate Guassian pyramid for apple
orange_copy=orange.copy()
gp_orange=[orange_copy]

for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#generate laplacian pyramid for apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    gau_extended = cv2.pyrUp(gp_apple[i])
    lapla = cv2.subtract(gp_apple[i - 1], gau_extended)
    lp_apple.append(lapla)

#generate laplacian pyramid for orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    gau_extended = cv2.pyrUp(gp_orange[i])
    lapla = cv2.subtract(gp_orange[i - 1], gau_extended)
    lp_orange.append(lapla)

#now add left and right halves of images in each level
apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple, lp_orange):
    n+=1
    col,rows,ch=apple_lap.shape
    lapla=np.hstack((apple_lap[:, 0:int(col/2)], orange_lap[:, int(col/2):]))
    apple_orange_pyramid.append(lapla)


# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
