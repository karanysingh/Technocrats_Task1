import cv2
import numpy as np
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        global a
    def __del__(self):
        self.video.release()
    def output():
        return a
    def get_frame(self):
        while True:
            a='No green ball found'
            lower_green = np.array([45, 140, 50])
            upper_green = np.array([75, 255, 255])
            success, frame = self.video.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv = cv2.medianBlur(hsv, 5)
            imgThreshHighgreen = cv2.inRange(hsv, lower_green, upper_green)
            circlesgreen = cv2.HoughCircles(imgThreshHighgreen, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30,minRadius=0, maxRadius=0)

            if circlesgreen is not None:
                a='Green ball Found!!'
                cv2.putText(frame,"BAll FOUND",org = (50, 50),fontFace = cv2.FONT_HERSHEY_SIMPLEX,thickness=2,fontScale=1,color = (255, 0, 0) )
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ret, jpeg = cv2.imencode('.jpg', frame)
            # self.output(a)
            return jpeg.tobytes(),a
            ###########################################################################
##while True:
# VideoCamera().get_frame()
