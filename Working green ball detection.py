import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

lower_green = np.array([45,140,50]) 
upper_green = np.array([75,255,255])

while(True):
    success,frame = cap.read()  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.medianBlur(hsv,5)
    imgThreshHighgreen = cv2.inRange(hsv, lower_green, upper_green)
    circlesgreen = cv2.HoughCircles(imgThreshHighgreen,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circlesgreen is not None:
            print ("found green")
    cv2.imshow('face',frame)
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
