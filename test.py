from utils.robot2 import *
import time
from math import *


robot = Robot(0,0,90)

try:
    robot.setServoPosition(0.1)
    time.sleep(0.1)
    robot.setServoPosition(0)
except KeyboardInterrupt:
    robot.setServoPosition(0)
    robot.stop()
