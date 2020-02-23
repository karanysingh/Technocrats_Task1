# Technocrats Task 1
The webpage displays the camera feed from the webcam(or video/URL).

## To clone this repo locally
* `git clone https://github.com/karanysingh/Technocrats_Task1`
* `cd Technocrats_Task1` 
* run `python main.py` in terminal.
* open `http://127.0.0.1:5000/` in the browser.

## To use a video or URL 
* simply replace `self.video = cv2.VideoCapture(0)` by 
`self.video = cv2.VideoCapture('URL/filename/path')` in **camera.py**.

* _Note_- 0 represents the default camera.
## Libraries used
* numpy
* opencv
* pySerial
* flask
![Screenshot](/templates/screenshot.png)

