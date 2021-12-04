from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main ():
    robot = Robot(0, 0, 90)
	return ''

@app.route('/drive')
def drive ():
	return ''

@app.route('/drive/<int:room>')
def driveToRoom (room):
	return ''

@app.route('/video')
def videoLibrary ():
	return ''

if __name__ == "__main__":
    app.run(debug=True)
