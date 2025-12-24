import cv2
import numpy as np

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg")

threshold_value = 200
_,binary_theshold = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow("Original ", img)
cv2.imshow("Threshold", binary_theshold)
cv2.waitKey(0)
cv2.destroyAllWindows()