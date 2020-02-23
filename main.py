from flask import Flask, render_template, Response,jsonify,send_file
from camera import VideoCamera
app = Flask(__name__)
arr=[]
vals =[]
corner = []
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    global arr,vals,corner
    while True:
        frame,a,threeArea,cor = camera.get_frame()
        if("*************Green ball Found!!***************" in arr):
            arr.append("*************Green ball Found!!***************"*5)
        #ball_status array
        arr = arr[len(arr)-1:len(arr)-1]
        arr.append(a)
        #Area array
        area = round((((threeArea/4) / (307200)) * 100),2)
        vals = vals[len(vals)-5:]
        vals.append(area)
        #corner array
        corner = corner[len(corner)-1:len(corner)-1]
        corner.append(cor)
        # print(arr)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
# def live(camera):
#
#     while True:
#         frame,a=camera.get_frame()
#         # yield(aa


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/params')
def params():
    ##return Response(live(VideoCamera),mimetype='text/event-stream')
    # # return jsonify(live(VideoCamera()
    # if ("*************Green ball Found!!***************" in arr):
    #     arr.append("*************Green ball Found!!***************")
    print(arr)
    return jsonify({'arr':arr})

@app.route('/params2')
def params2():

    print(vals)
    return jsonify({'vals':round(sum(vals)/3,2)})

@app.route('/params3')
def params3():
    print(corner)
    return jsonify({'corner':corner})

#Passes image to html

@app.route('/banner')
def get_image():
    filename = 'templates/technocrats.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/back')
def get_back():
    filename = 'templates/codewall.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/font')
def get_font():
    filename = 'templates/OrionPax.ttf'
    return send_file(filename, mimetype='font/ttf')

app.run(debug=True)
