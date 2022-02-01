from utils.robot2 import *
import time
from math import *


robot = Robot(0,0,90)

try:
    robot.setServoPosition(0.5)
except KeyboardInterrupt:
    robot.stop()
