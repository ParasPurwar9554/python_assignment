import cv2
import numpy as np

video = cv2.VideoCapture("D:/My Python Projects/Open CV/nature_sample.mp4")

while video.isOpened():
    _,frame = video.read()
    frame = cv2.resize(frame,(700,720))
    cv2.imshow("frame ", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

cv2.destroyAllWindows()