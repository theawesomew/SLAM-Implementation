from utils.robot2 import *
import time


robot = Robot(0,0,90)

try:
    robot.forward(1)
    time.sleep(1)
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
