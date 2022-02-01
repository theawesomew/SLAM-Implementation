from utils.robot2 import *
import time
from math import *


robot = Robot(0,0,90)

try:
    robot.turn(True)
    time.sleep(1)
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
