import cv2

img = cv2.imread("D:/My Python Projects/Open CV/highway.jpg",0)
print("Dimention of Image ", img.shape)

width = img.shape[1]
height = 300

dim = (width,height)
resized = cv2.resize(img,dim)

if img is None:
    print("Image Not Found!")
cv2.imshow("window",resized)
cv2.imwrite("car.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()