from utils.robot2 import *
import time
import sys
from math import *

robot = Robot(0,0,90,0.9,0.9)

try:
    robot.setServoPosition(0.5)
    time.sleep(float(sys.argv[1]))
    robot.setServoPosition(0)
    robot.setServoPosition(-0.15)
    time.sleep(float(sys.argv[1]))
    robot.setServoPosition(0)
except KeyboardInterrupt:
    robot.setServoPosition(0)
    robot.stop()
