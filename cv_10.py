import cv2

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg")
resize = cv2.resize(img,(440,440))
kernal = 3

blur = cv2.medianBlur(resize,kernal)

cv2.imshow("Original ", img)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

