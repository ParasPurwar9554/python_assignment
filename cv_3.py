import cv2
import numpy as np

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg")

width = 350
height = 300

dim = (width,height)
resized = cv2.resize(img,dim)
print("Image Size In Bytes : ",img.size)
cv2.imshow("Original ", resized)
#flip = cv2.flip(resized,1)
#cv2.imshow("Horizentaly ",flip)

#flip1 = cv2.flip(resized,0)
#cv2.imshow("Vertically ",flip1)

flip2 = cv2.flip(resized,-1)
cv2.imshow("Vertically ",flip2)
cv2.waitKey(0)
cv2.destroyAllWindows()