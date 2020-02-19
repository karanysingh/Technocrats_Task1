# Technocrats Task 1
The webpage displays the camera feed from the webcam(or video/URL).

## To clone this repo locally
* `git clone https://github.com/karanysingh/Technocrats_Task1`
* run `python main.py` in terminal.

## To use a video or URL 
* simply replace `self.video = cv2.VideoCapture(0)` by 
`self.video = cv2.VideoCapture('URL/filename/path')` in **camera.py**.

* _Note_- 0 represents the default camera.
## Libraries used
* numpy
* opencv
* pySerial
* flask

