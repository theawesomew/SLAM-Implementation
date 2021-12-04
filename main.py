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
    return 'Currently driving'

@app.route('/drive/<int:room>', methods=["get"])
def driveToRoom (room):
	return ''

@app.route('/video')
def videoLibrary ():
	return ''

if __name__ == "__main__":
    app.run(debug=True)
