import cv2

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg")

resize = cv2.resize(img,(440,440))

ksize = (7,7)
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow("Original ", img)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()