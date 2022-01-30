from utils.robot2 import *
import time


robot = Robot(0,0,90)

try:
    secondsPerDegree = (1/(2*degrees(asin(9/18.25))))*2.25
    robot.turn(True)
    time.sleep(secondsPerDegree * 90)
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
