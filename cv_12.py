import cv2
import numpy as np

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg",0)

resize = cv2.resize(img,(440,440))

min_thresh = 100
max_thresh = 200

edges = cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow("Original ", img)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()