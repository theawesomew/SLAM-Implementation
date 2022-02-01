from utils.robot2 import *
import time
from math import *


robot = Robot(0,0,90,0.9,0.9)

try:
    robot.setServoPosition(0.5)
    time.sleep(2)
    robot.setServoPosition(0)
except KeyboardInterrupt:
    robot.setServoPosition(0)
    robot.stop()
