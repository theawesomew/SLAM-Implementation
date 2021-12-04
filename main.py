from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
import time
from flask import Flask, request

app = Flask(__name__);

@app.route('/')
def main ():
	robot = Robot(0, 0, 90)
	return '<!DOCTYPE html><html><head><meta charset="UTF-8"/><title></title><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script></head><body><div class="container-fluid"><div class="row"><a href="/drive">Drive To</a></div><div class="row"><a href="/door">Door Activation</a></div><div class="row"><a href="/video">Video Library</a></div></div></body></html>'

@app.route('/drive')
def drive ():
	try:
		robot.follow("FFFF")
		robot.stop()
	except KeyboardInterrupt:
		robot.stop()
		print("Program terminated")

@app.route('/drive/<int:room>')
def driveToRoom (room):
	return ''

@app.route('/video')
def videoLibrary ():
	return ''

if __name__ == "__main__":
    app.run(debug=True)
