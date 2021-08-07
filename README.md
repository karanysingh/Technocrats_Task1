# Technocrats Task 1
* GreenBall detection using `python` `opencv`. A feed is provided to the webpage using `flask` with basic details like
 > closest corner of screen, percentage of area covered by ball etc.
* Depending on whether ball is detected or not red or green light blinks of the connected arduino.[`serial communication`]
* The basic UI is build using HTML CSS.

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
#
![Screenshot](/templates/screenshot.png)

