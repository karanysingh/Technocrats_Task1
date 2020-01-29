import cv2
import time
from imutils.video import VideoStream
#t,y = cv2.VideoCapture(0).read()
#cv2.imshow('frame',y)
#cv2.waitKey(0)
vs = cv2.VideoCapture(0)
time.sleep(2.0)
while True:
    print("HI")
    frame = vs.read()
    cv2.imshow('Screen',frame[1])
    i=cv2.waitKey(1)
    if i == 27:
        break
