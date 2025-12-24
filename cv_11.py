import cv2

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg")

resize = cv2.resize(img,(440,440))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow("Original ", img)
cv2.imshow("b",b)
cv2.waitKey(0)
cv2.destroyAllWindows()