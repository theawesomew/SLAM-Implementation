from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
import time
from flask import Flask, request, render_template

app = Flask(__name__)
robot = ''

@app.route('/')
def main ():
    global robot
    robot = Robot(0, 0, 90)
    return render_template('index.html')

@app.route('/drive')
def drive ():
    return render_template('drive.html')

@app.route('/drive/<int:room>', methods=["get"])
def driveToRoom (room):
    global robot
    programString = ""

    if room == 1:
        programString = "F"*(1920//150+1) + "R"*(720//150+1)
    elif room == 2:
        programString = "F"*(400//80+1) + "R"*(1400//150+1)
    else:
        programString = "F"*(7340//150+1) + "R"*(1340//150+1)

    robot.follow(programString)
    robot.stop()

    return ''

@app.route('/video')
def videoLibrary ():
	return render_template("video.html")

if __name__ == "__main__":
    app.run(debug=True)
