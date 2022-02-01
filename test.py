from utils.robot2 import *
import time


robot = Robot(0,0,90)

try:
    robot.setServoPosition(0.5)
except KeyboardInterrupt:
    robot.stop()
