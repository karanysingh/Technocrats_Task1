"""     CAMERA MODULE
captures the camera frames then displays 'Green Ball Found' on the frame if it detects a 'green ball' in the frame.
"""


import cv2
import numpy as np
class VideoCamera(object):
    #constructor
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        global a
        
    #destructor
    def __del__(self):
        self.video.release()
        
    #flask imports 'green ball found' through this function
    def output():
        return a
    
    #Finds the 'green ball' and prints it on the frame
    def get_frame(self):
        while True:
            a='No green ball found'
            #RANGES OF ACCEPTED GREEN SHADES
            lower_green = np.array([45, 140, 50])
            upper_green = np.array([75, 255, 255])
            
            #READING FRAMES
            success, frame = self.video.read()
            
            #CONVERTING FRAMES TO HSV(and applying median blur for better detection)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv = cv2.medianBlur(hsv, 5)
            
            #Extracts the green region
            imgThreshHighgreen = cv2.inRange(hsv, lower_green, upper_green)
             
            #Extracts the circles from filtered frame 'imgThreshHighgreen'
            circlesgreen = cv2.HoughCircles(imgThreshHighgreen, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30,minRadius=0, maxRadius=0)
            
            #Puts 'Green Ball found' on the frame.
            if circlesgreen is not None:
                a='Green ball Found!!'
                cv2.putText(frame,"Green Ball Found!!",org = (50, 50),fontFace = cv2.FONT_HERSHEY_SIMPLEX,thickness=2,fontScale=1,color = (255, 0, 0) )
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            # self.output(a)
            return jpeg.tobytes(),a
###########################################################################
##while True:
# VideoCamera().get_frame()
