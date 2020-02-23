"""     CAMERA MODULE
captures the camera frames then displays 'Green Ball Found' on the frame if it detects a 'green ball' in the frame.
"""


import cv2
import numpy as np
import serial
import time
class VideoCamera(object):
    a ="not found"
    #constructor
    def __init__(self):
        self.video = cv2.VideoCapture(0,cv2.CAP_V4L)
        global a

    #destructor
    def __del__(self):
        self.video.release()
    def corner(self,img,x,y,r):
        centerX = (img.shape[0])/2
        centerY = (img.shape[1])/2
        if(x<centerX and y<centerX):
            return("Top left Corner")
        elif(x>centerX and y>centerX):
            return("Bottom right Corner")
        elif(x>centerX and y<centerX):
            return("Top Right Corner")
        else:
            return("Bottom Left Corner")

    def area(self,img,t,threeArea,r):
        # print(r)
        area = cv2.countNonZero(img)
        if t<3 and (area>0):
            # print('got!')
            threeArea+=area
            t+=1
            # print(t)
            return t,threeArea
        else:
            print("ball Found covering %0.2lf percent area" % ((((threeArea/4) / (img.size)) * 100)))
            t=0
            threeArea = 0
            return t,threeArea

    #Finds the 'green ball' and prints it on the frame
    def get_frame(self):
        t = 0
        threeArea=0
        while True:
            try:
                ser = serial.Serial('/dev/ttyACM0',9600)
            except:
                ser = serial.Serial('/dev/ttyUSB0',9600)
            ser.write('L'.encode())#turns built in led 'off'
            a='Not Found'
            #RANGES OF ACCEPTED GREEN SHADES
            lower_green = np.array([45, 140, 50])
            upper_green = np.array([75, 255, 255])
            # lower_green = np.array([25, 52, 72])
            # upper_green = np.array([102, 255, 255])

            #READING FRAMES
            success, frame = self.video.read()

            #CONVERTING FRAMES TO HSV(and applying median blur for better detection)q
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv = cv2.medianBlur(hsv, 5)

            #Extracts the green region
            imgThreshHighgreen = cv2.inRange(hsv, lower_green, upper_green)

            #Extracts the circles from filtered frame 'imgThreshHighgreen'
            circlesgreen = cv2.HoughCircles(imgThreshHighgreen, cv2.HOUGH_GRADIENT, 1, 20, param1=2, param2=30,minRadius=0, maxRadius=0)
            # print(circlesgreen)
            cor = "Nearest Corner"
            #Puts 'Green Ball found' on the frame.
            if circlesgreen is not None:
                a='FOUND!!'
                img = imgThreshHighgreen
                t,threeArea = self.area(img,t,threeArea,circlesgreen[0][0][2])
                cor = self.corner(img,circlesgreen[0][0][0],circlesgreen[0][0][1],circlesgreen[0][0][2])
                print(a)
                # print("ball Found covering %d percent area" %((((area)/(img.size))*100)))
                ser.write('H'.encode())#turns built in led 'on'
                # time.sleep(1)
                cv2.putText(frame,"BALL",org = tuple(circlesgreen[0][0][0:2]),fontFace = cv2.FONT_HERSHEY_SIMPLEX,thickness=2,fontScale=1,color = (255, 0, 0) )
                #cv2.putText(frame,"Green Ball Found!!",org = (50, 50),fontFace = cv2.FONT_HERSHEY_SIMPLEX,thickness=2,fontScale=1,color = (255, 0, 0) )
            # cv2.imshow('frame', imgThreshHighgreen)
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes(),a,threeArea,cor
###########################################################################
# VideoCamera().get_frame()
