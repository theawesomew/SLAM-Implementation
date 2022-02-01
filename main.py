from utils.robot2 import *
from utils.mapping import *
from utils.pathfinding import *
from flask import Flask, request, render_template
import time
import sys

# connect the robot to the internet using 'sudo netplan apply'
# navigate to the SLAM-Implementation directory using 'cd SLAM-Implementation'
# pull the latest changes using 'sudo git pull'
# 

app = Flask(__name__)
robot = ''
leftPower, rightPower = 0.9, 0.9

if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg.startswith("L") or arg.startswith("l"):
            leftPower = float(arg[1:]/100)
        elif arg.startswith("R") or arg.startswith("r"):
            rightPower = float(arg[1:]/100)

@app.route('/')
def main ():
    global robot
    robot = Robot(0, 0, 90, leftPower, rightPower)
    return render_template('index.html')

@app.route('/drive')
def drive ():
    return render_template('drive.html')

@app.route('/drive/<int:room>', methods=["get"])
def driveToRoom (room):
    global robot
    programString = ""

    if room == 1:
        programString = "F"*(1920//300+1) + "R"*(720//300+1)
    elif room == 2:
        programString = "F"*(400//300+1) + "R"*(1400//300+1)
    elif room == 3:
        programString = "F"*(7340//300+1) + "R"*(1340//300+1)
    elif room == 4:
        programString = "FR"
    elif room == 6:
        programString = "FF"
    else:
        programString = ""
        robot.turn(True)
        time.sleep(5)

    robot.follow(programString)
    robot.stop()

    return ''

@app.route('/video')
def videoLibrary ():
	return render_template("video.html")

@app.route('/video/<int:videoID>', methods=["get"])
def getVideo (videoID):
    return render_template(f"video_{videoID}.html")

if __name__ == "__main__":
    app.run(debug=True)
