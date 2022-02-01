from utils.robot2 import *
import time
from math import *


robot = Robot(0,0,90)

try:
    robot.forward(1)
    time.sleep(1)
    robot.turn(True)
    time.sleep(90 * (1/(2*degrees(asin(9/18.25)))))
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
